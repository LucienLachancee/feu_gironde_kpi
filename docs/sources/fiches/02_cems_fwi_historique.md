# Fiche 02 — Copernicus CEMS : indices de danger feu historiques (FWI)

Requête réelle le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | ECMWF pour Copernicus EMS (CEMS), au compte du JRC (EFFIS). |
| Accès (URL) | https://ewds.climate.copernicus.eu/datasets/cems-fire-historical-v1 ; API `cdsapi`, jeu `cems-fire-historical-v1` ; DOI 10.24381/cds.0e89c522. **Compte et clé d'API requis** (`~/.cdsapirc` ou `CDSAPI_URL` / `CDSAPI_KEY`), créés par l'équipe, jamais commités. Requête test aboutie (ID `d25d1ede-…`, 20 s) ; requête 2026 restée plus de 10 min en file d'attente. |
| Contenu | NetCDF4 (converti de GRIB par cfgrib), variable `fwinx` (FWI, Canadian Forest Service), dimensions `valid_time × latitude × longitude`. 14 indices disponibles ; seul le FWI est demandé (minimisation). 33 Ko par mois sur la zone (≈ 7 Mo pour 20 ans). SHA-256 du fichier test : `d37dfce3a43efb17…`. |
| Granularité | **Maille 0,25° × jour** (≈ 28 × 20 km). Zone 43,25-45,75 °N, 1,5 °O-0,5 °E : 99 mailles, dont des mailles en mer (valeurs non masquées). |
| Historique | Du 03/01/1940 au 14/11/2026 (métadonnées). Test juillet 2022 : 31 jours, 0 manquant, FWI de 0,06 à 77,4 ; 40 à 50 sur le massif le 12/07/2022. |
| Fraîcheur | Réanalyse ERA5 : danger **observé a posteriori**, pas une prévision J+1. Avertissement de l'API : mises à jour arrêtées à partir du 16/11/2026 (obstacle O06). |
| Clés | (date, latitude, longitude) ; aucun code commune : correspondance maille ↔ commune à construire. |
| Licence | **CC-BY 4.0** (métadonnées, lien SPDX) ; acceptation sur le compte requise. |
| Millésime | `system_version 4_1`. |
| Référentiel géographique | Grille régulière WGS84 0,25°. |
| Données personnelles | Aucune. |
| Questions servies | Q1 (danger historique par zone et par jour), Q3 (danger du jour de chaque départ). |
| Premiers constats qualité | Mailles marines à exclure ; latitudes en ordre décroissant ; temps en secondes depuis 1970. |
| Décision | **Retenue** : couvre le danger du jour de chaque départ (Q3) et le danger historique par maille (Q1). |
