# Feux de forêt Gironde — pipeline décisionnel (UE01.A)

Pipeline raw → staging → intermédiaire → marts et entrepôt en étoile au service des décisions du
SDIS 33 (commanditaire supposé, D01) face aux grands feux de forêt.

```bash
docker compose run --rm app make all          # avec Docker
uv venv .venv && uv pip install --python .venv/bin/python -r requirements.txt && make all   # sans Docker
```

| Cible | Rôle |
|---|---|
| `make ingest` | téléchargement, provenance, chargement raw |
| `make build` | `dbt seed` + `dbt run` |
| `make test` | tests dbt |
| `make docs` | `dbt docs generate` |
| `make all` | les quatre dans l'ordre |
| `make clean` | supprime la base et les artefacts dbt |

Décisions : `docs/journal_decisions.md` · obstacles : `docs/obstacles.md`.
