# Obstacles rencontrés

## O01 — dbt absent de l'environnement de développement (T0)

- **Constat** : `dbt: command not found`.
- **Cause** : environnement fourni sans dbt.
- **Impact** : `make all` invérifiable sans installation.
- **Contournement** : venv local `.venv` créé avec `uv`, versions épinglées de `requirements.txt`. Le `Makefile` utilise `.venv/bin/*` s'il existe, sinon les outils du `PATH` (image Docker).
- **Statut** : résolu.

## O02 — Docker non disponible pour la vérification (T0)

- **Constat** : `docker compose run --rm app make all` ne peut pas être exécuté dans l'environnement de développement.
- **Cause** : environnement de développement conteneurisé, sans Docker.
- **Impact** : l'exécution sous Docker est `non vérifié` (Docker absent).
- **Contournement** : `make all` vérifié avec le venv ; le `Dockerfile` installe le même `requirements.txt`.
- **Statut** : ouvert (test de `docker compose` à faire sur un poste avec Docker).
