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

## O03 — BDIFF : chaîne de certificats TLS incomplète (T2)

- **Constat** : `curl: (60) SSL certificate problem: unable to get local issuer certificate` sur `bdiff.agriculture.gouv.fr` (idem avec `requests`).
- **Cause** (`openssl s_client`) : certificat émis par « GEANT TLS RSA 1 » (HARICA) présenté avec un mauvais intermédiaire (« GEANT OV RSA CA 4 », Sectigo/USERTrust).
- **Impact** : téléchargement BDIFF impossible sans correction.
- **Contournement** : intermédiaire correct téléchargé depuis l'URL AIA (`http://crt.harica.gr/HARICA-GEANT-TLS-R1.cer`) et ajouté au magasin `certifi` ; chaîne validée jusqu'à « HARICA TLS RSA Root CA 2021 ». Vérification TLS maintenue (pas de `verify=False`).
- **Statut** : contourné (automatisé dans l'ingestion) ; à signaler au producteur (contact indiqué dans les mentions légales).

## O04 — BDIFF : licence contradictoire (T2)

- **Constat** : data.gouv.fr affiche « Licence Ouverte v2.0 » ; les mentions légales du zip (§7) interdisent la vente, exigent « l'intégrité des données (aucune modification) » et indiquent que « les droits de reproduction sont réservés et strictement limités ».
- **Cause** : deux licences différentes publiées pour le même jeu.
- **Impact** : usage commercial exclu ; transformation des données contestable.
- **Contournement** : usage pédagogique et non commercial ; fichier brut conservé intact (raw, SHA-256) ; tables dérivées citant « Source : BDIFF, bdiff.agriculture.gouv.fr ». Licence notée « contradictoire » dans la fiche.
- **Statut** : documenté, non levé (question à poser au producteur avant tout usage hors du cours).

## O05 — DuckDB 2.0.0 : résultats faux sur un filtre spatial (T2)

- **Constat** : duckdb 2.0.0 + spatial, couche végétation BD TOPO : `count(*) where nature in (…) and st_area(geom) >= 1e5` renvoie 10, contre 3 190 avec `sum(case when … then 1 else 0 end)` ; `where st_area(geom) >= 1e5` seul renvoie 109 lignes, contre 9 070.
- **Cause** : défaut probable de la 2.0.0 (optimisation des filtres), non investigué plus loin. Sous duckdb 1.4.5, les deux formulations donnent 3 190 et 9 070.
- **Impact** : calculs spatiaux faux.
- **Contournement** : duckdb épinglé en 1.4.5 dans `requirements.txt` (compatible dbt-duckdb 1.11.1) ; calculs de T2 refaits en 1.4.5. Tout résultat surprenant est vérifié par un second calcul indépendant.
- **Statut** : résolu.

## O06 — Copernicus CEMS : arrêt des mises à jour et file d'attente variable (T2)

- **Constat** : avertissement de l'API « *On Monday, 16th November 2026, updates to this dataset will cease until further notice. A new mars configuration is required…* ». Requête de 31 jours : 20 s ; requête sur 2026 : plus de 10 min en file.
- **Cause** : arrêt annoncé par le producteur ; variabilité de la file non expliquée par l'API.
- **Impact** : pas de données après mi-novembre 2026 ; durée de `make ingest` imprévisible.
- **Contournement** : une requête par année, mise en cache dans `data/raw` (année chargée non redemandée) ; délai d'attente long ; clé absente ou API muette → source journalisée `unavailable`, pipeline poursuivi (modèles vides, tests en alerte).
- **Statut** : contourné ; reprise des mises à jour à surveiller.

## O07 — EFFIS : certificat TLS expiré (T2)

- **Constat** : `curl: (60) SSL certificate problem: certificate has expired` sur `data.effis.emergency.copernicus.eu` (cible de la redirection). Deux essais le 17/11/2026.
- **Cause** : certificat valide du 27/04/2026 au 11/11/2026 (openssl).
- **Impact** : fichier non téléchargé ; aucune décision du SDIS n'en dépend (contexte Saumos 2026 seulement).
- **Contournement** : vérification TLS maintenue (authenticité non garantie sinon) ; fiche remplie avec `non vérifié` ; source écartée du pipeline v0.1.
- **Statut** : à réessayer après renouvellement du certificat.

## O08 — IFM horaire communautaire et Prométhée inaccessibles (T2)

- **Constat** : IFM horaire (`open-ifm.b-cdn.net`) : HTTP 403 « *Domain suspended or not configured* » ; Prométhée (`www.promethee.com`) : certificat ne correspondant pas au nom de domaine.
- **Cause** : domaine suspendu (IFM) ; certificat d'un autre domaine (Prométhée).
- **Impact** : nul : sources déjà candidates au rejet (qualité non garantie ; hors emprise).
- **Contournement** : rejet argumenté dans les fiches 05 et 13.
- **Statut** : documenté.
