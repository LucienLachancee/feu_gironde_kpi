"""Socle d'ingestion : téléchargement, provenance, registre des fichiers et journal de chargement.

Idempotence : chaque fichier est haché (SHA-256) ; un couple (source, sha256) déjà présent dans
raw.ingestion_registry n'est pas rechargé. Chaque tentative écrit une ligne dans raw.load_log.
Le chargement d'un fichier et son inscription au registre forment une seule transaction.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import shutil
import tempfile
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, NamedTuple

import duckdb
import requests

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
DB_PATH = Path(os.environ.get("FEU_DUCKDB_PATH", ROOT / "data" / "warehouse" / "feu_gironde.duckdb"))
USER_AGENT = "feu-gironde-kpi/0.1 (projet pedagogique)"
RUN_ID = uuid.uuid4().hex[:12]


class RawFile(NamedTuple):
    source_id: str
    path: Path
    sha256: str


@dataclass
class Source:
    source_id: str
    licence: str
    millesime: str
    file_name: str
    fetch: Callable[[Path], tuple[Path, str] | None]  # -> (fichier téléchargé, URL) ou None
    load: Callable[[duckdb.DuckDBPyConnection, RawFile], int]  # -> lignes chargées
    immutable: bool = False  # édition figée : jamais retéléchargée une fois chargée


def utcnow() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def local_copy(source_id: str, file_name: str) -> Path | None:
    """Fichier déjà stocké en raw pour cette source (évite de retélécharger une édition figée)."""
    found = sorted((RAW_DIR / source_id).glob(f"*/{file_name}"))
    return found[-1] if found else None


def http_download(url: str, dest: Path, timeout: int = 300, attempts: int = 6) -> Path:
    """Téléchargement en flux, repris là où il s'est arrêté après une coupure (en-tête Range, O09)."""
    for attempt in range(1, attempts + 1):
        done = dest.stat().st_size if dest.exists() else 0
        headers = {"User-Agent": USER_AGENT, **({"Range": f"bytes={done}-"} if done else {})}
        try:
            with requests.get(url, stream=True, timeout=timeout, headers=headers) as r:
                r.raise_for_status()
                resumed = r.status_code == 206
                expected = int(r.headers["Content-Range"].split("/")[-1]) if resumed else \
                    int(r.headers.get("Content-Length", -1))
                with open(dest, "ab" if resumed else "wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
            if expected < 0 or dest.stat().st_size == expected:
                return dest
            raise IOError(f"taille reçue {dest.stat().st_size} ≠ annoncée {expected}")
        except (requests.RequestException, IOError) as exc:
            if attempt == attempts:
                raise
            print(f"   … coupure ({type(exc).__name__}), reprise {attempt}/{attempts - 1}", flush=True)
            time.sleep(5 * attempt)
    return dest


def connect(ddl: list[str]) -> duckdb.DuckDBPyConnection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect(str(DB_PATH))
    con.execute("install spatial; load spatial; create schema if not exists raw")
    for stmt in ddl + [
        """create table if not exists raw.ingestion_registry (
            source_id varchar not null, sha256 varchar not null, file_name varchar not null,
            raw_path varchar not null, source_url varchar not null, downloaded_at timestamptz not null,
            licence varchar not null, millesime varchar not null, n_rows bigint not null,
            loaded_at timestamptz not null, primary key (source_id, sha256))""",
        # status : loaded | skipped_known_hash | skipped_immutable | unavailable | error
        """create table if not exists raw.load_log (
            run_id varchar not null, source_id varchar not null, sha256 varchar, status varchar not null,
            n_rows bigint, message varchar, started_at timestamptz not null, finished_at timestamptz not null)""",
    ]:
        con.execute(stmt)
    return con


def ingest_source(con: duckdb.DuckDBPyConnection, source: Source) -> None:
    started = utcnow()

    def log(sha, status, n_rows, message):
        con.execute("insert into raw.load_log values (?, ?, ?, ?, ?, ?, ?, ?)",
                    [RUN_ID, source.source_id, sha, status, n_rows, message, started, utcnow()])
        print(f"[ingest] {source.source_id} -> {status} {n_rows if n_rows is not None else ''} {message or ''}", flush=True)

    known = con.execute("select max(sha256) from raw.ingestion_registry where source_id = ?",
                        [source.source_id]).fetchone()[0]
    if source.immutable and known:
        return log(known, "skipped_immutable", 0, "édition figée déjà chargée")

    (RAW_DIR / "_tmp").mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="ingest_", dir=RAW_DIR / "_tmp"))
    try:
        try:
            fetched = source.fetch(tmp)
            reason = "source indisponible (docs/obstacles.md)"
        except Exception as exc:  # réseau, HTTP, API : le pipeline continue sans cette source
            fetched, reason = None, f"échec du téléchargement : {type(exc).__name__}: {exc}"[:500]
        if fetched is None:
            return log(None, "unavailable", None, reason)
        path, url = fetched
        sha = sha256_of(path)
        if con.execute("select count(*) from raw.ingestion_registry where source_id = ? and sha256 = ?",
                       [source.source_id, sha]).fetchone()[0]:
            return log(sha, "skipped_known_hash", 0, "fichier déjà chargé")

        # Fichier stocké tel quel, avec sa provenance
        dest = RAW_DIR / source.source_id / sha[:16] / source.file_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.resolve() != dest.resolve():
            shutil.copyfile(path, dest)
        prov_file = dest.parent / "provenance.json"
        if prov_file.exists():  # fichier déjà stocké : sa provenance d'origine fait foi
            prov = json.loads(prov_file.read_text())
        else:
            prov = {"source_id": source.source_id, "source_url": url, "downloaded_at": utcnow().isoformat(),
                    "sha256": sha, "licence": source.licence, "millesime": source.millesime,
                    "raw_path": str(dest.relative_to(RAW_DIR))}
            prov_file.write_text(json.dumps(prov, ensure_ascii=False, indent=2))
        downloaded_at = dt.datetime.fromisoformat(prov["downloaded_at"])
        url = prov["source_url"]

        con.execute("begin transaction")
        try:
            n = source.load(con, RawFile(source.source_id, dest, sha))
            con.execute("insert into raw.ingestion_registry values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        [source.source_id, sha, source.file_name, prov["raw_path"], url, downloaded_at,
                         source.licence, source.millesime, n, utcnow()])
            con.execute("commit")
        except Exception:
            con.execute("rollback")
            raise
        log(sha, "loaded", n, None)
    except Exception as exc:
        log(None, "error", None, f"{type(exc).__name__}: {exc}"[:500])
        raise
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
