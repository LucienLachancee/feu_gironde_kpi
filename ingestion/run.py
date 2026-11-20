"""Point d'entrée : `python -m ingestion.run [source_id ...]` (toutes les sources par défaut)."""

import sys

from ingestion.common import connect, ingest_source
from ingestion.sources import DDL, SOURCES

wanted = sys.argv[1:]
con = connect(DDL)
for source in SOURCES:
    if not wanted or source.source_id in wanted:
        ingest_source(con, source)
con.close()
