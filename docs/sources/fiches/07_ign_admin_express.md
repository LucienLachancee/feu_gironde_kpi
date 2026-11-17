# Fiche 07 — ADMIN EXPRESS COG CARTO (édition 2026), IGN

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | IGN. |
| Accès (URL) | https://www.data.gouv.fr/datasets/admin-express-admin-express-cog-admin-express-cog-carto-admin-express-cog-carto-pe-admin-express-cog-carto-plus-pe ; `https://data.geopf.fr/telechargement/download/ADMIN-EXPRESS-COG-CARTO/ADMIN-EXPRESS-COG-CARTO_4-0__GPKG_LAMB93_FXX_2026-01-01/…7z`. Public, sans compte. |
| Contenu | Contours **généralisés** des communes (code INSEE, nom, statut, population, date du recensement, codes supra-communaux). 7z (64 Mo) → GeoPackage 293 Mo ; couches commune (34 746), département, canton, EPCI, chefs-lieux… SHA-256 : `b5dc8d8dbdc37228…`. |
| Granularité | Commune au 01/01/2026. |
| Historique | Une édition par an ; seule l'édition 2026 est ouverte. |
| Fraîcheur | Annuelle, alignée sur le COG ; métadonnées datées du 30/06/2026. |
| Clés | `code_insee`. |
| Licence | Licence Ouverte 2.0 selon data.gouv.fr ; le LISEZ-MOI dit seulement que « la plupart des produits sont … en licence ouverte » : licence exacte `non vérifié` dans le fichier. |
| Millésime | 2026 (`ED2026-01-01`). |
| Référentiel géographique | COG 2026, Lambert 93 (EPSG:2154), comme la BD TOPO et la BD Forêt. 534 communes en Gironde (1 008 819 ha), 327 dans les Landes : identique au COG 2026. |
| Données personnelles | Aucune. |
| Questions servies | Q1 (centroïde de commune → maille FWI), Q4 (rattacher bâti et végétation aux communes). |
| Premiers constats qualité | `population` (recensement 2023) identique à la population municipale INSEE pour les 861 communes 33 + 40 : redondant avec la fiche 11. Surfaces approchées : écart de 0,8 % avec la synthèse BD Forêt (1 008 819 ha contre 1 016 955 ha). |
| Décision | **Retenue** : indispensable aux jointures spatiales (contours, centroïdes). |
