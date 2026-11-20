# Fiche 10 — Capacités d'hébergement touristique, INSEE

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | INSEE (enquêtes de fréquentation et répertoires des hébergements classés, selon la page de diffusion). |
| Accès (URL) | https://www.insee.fr/fr/statistiques/2021703 ; jeu Melodi `https://api.insee.fr/melodi/file/DS_TOUR_CAP/DS_TOUR_CAP_2026_CSV_FR` (référencé sur data.gouv.fr). Public, sans compte. |
| Contenu | Zip (7,3 Mo) → `DS_TOUR_CAP_2026_data.csv` (131 Mo, format long SDMX, `;`) + `DS_TOUR_CAP_2026_metadata.csv`. Une ligne par (territoire, type de territoire, activité, classement, durée de séjour, mesure) : `ACTIVITY` I551 hôtels, I552 / I552A-C collectifs, I553 campings ; `TOUR_MEASURE` UNIT_LOC, PLACE, BEDPLACE ; `L_STAY` de passage / à l'année ; `UNIT_LOC_RANKING` 1 à 5 étoiles, NC, `_T`. Gironde : 33 038 emplacements de camping (dont 8 576 à l'année), 14 520 chambres d'hôtel. SHA-256 du zip : `b25119b975576f98…`. |
| Granularité | Commune (et 10 autres niveaux géographiques) × année. |
| Historique | Fichiers séparés 2015 → 2025 ; **rupture de format en 2024** (harmonisation européenne, table de passage fournie). |
| Fraîcheur | Annuelle (situation au 1er janvier). |
| Clés | `GEO` + `GEO_OBJECT` ('COM'). |
| Licence | Licence Ouverte 2.0 selon data.gouv.fr ; pas de mention dans le fichier. |
| Millésime | 2026 ; diffusé le 05/02/2026 en géographie 2025, **rechargé le 27/08/2026 en géographie 2026** (constaté sur la page). |
| Référentiel géographique | Géographie 2026 (fichier rechargé) ; 534 communes en Gironde, 327 dans les Landes ; 0 valeur vide. |
| Données personnelles | Pas de nom. Indirectement : un seul camping 4 étoiles dans une commune désigne un établissement (souvent une entreprise individuelle) ; donnée publique de classement, risque faible. |
| Questions servies | Q4 (proxy de la population saisonnière). |
| Premiers constats qualité | Totaux (`_T`) et détails dans la même colonne : double compte si l'on somme sans filtrer. Ne couvre ni les résidences secondaires, ni la location entre particuliers, ni le camping sauvage : proxy partiel. |
| Décision | **Retenue** comme proxy (hébergement marchand seulement, manque M4). |
