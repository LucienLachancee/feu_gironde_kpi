# Pipeline UE01.A — feux de forêt Gironde. Usage : make all (ou docker compose run --rm app make all)

# venv local s'il existe, sinon outils du PATH (conteneur Docker)
PYTHON ?= $(if $(wildcard .venv/bin),.venv/bin/python,python)
DBT    ?= $(if $(wildcard .venv/bin),.venv/bin/dbt,dbt)

export DBT_PROJECT_DIR := $(CURDIR)/dbt
export DBT_PROFILES_DIR := $(CURDIR)/dbt
export DBT_SEND_ANONYMOUS_USAGE_STATS := false
export FEU_DUCKDB_PATH := $(CURDIR)/data/warehouse/feu_gironde.duckdb

.PHONY: all ingest build test docs clean

all: ingest build test docs

ingest:     ## téléchargement, provenance, chargement raw (un fichier déjà chargé ne l'est pas deux fois)
	$(PYTHON) -m ingestion.run

build:      ## seeds + modèles staging, intermediate, marts
	$(DBT) seed
	$(DBT) run

test:       ## tests de qualité et de non-perte (error = bloque, warn = alerte)
	$(DBT) test

docs:       ## lineage (dbt docs)
	$(DBT) docs generate

clean:      ## supprime base et artefacts dbt (les fichiers bruts sont conservés)
	rm -rf dbt/target dbt/logs dbt/dbt_packages data/warehouse
