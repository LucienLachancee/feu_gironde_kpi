# Fiche 04 — Données climatologiques de base quotidiennes, Météo-France

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | Météo-France. |
| Accès (URL) | https://www.data.gouv.fr/datasets/donnees-climatologiques-de-base-quotidiennes ; fichier inspecté `Q_33_latest-2025-2026_RR-T-Vent.csv.gz` (+ `Q_descriptif_champs_RR-T-Vent.csv`). Par département et période (avant 1949, 1950-2024, 2025-2026), familles « RR-T-Vent » et « autres paramètres » (humidité). Public, sans compte. |
| Contenu | Pluie (RR), températures (TN, TX, TM…), vent (FFM, FXY, FXI…) ; CSV gzip `;`, 60 colonnes (valeur + code qualité `Q*`). 444 Ko (2025-2026), 16 Mo (1950-2024). SHA-256 : `0470ce2c72f54c42…`. |
| Granularité | **Station × jour** ; 21 stations en Gironde. |
| Historique | Fichier inspecté : 01/01/2025 → 15/11/2026, 14 364 lignes ; fichiers antérieurs depuis avant 1949. |
| Fraîcheur | Quotidienne pour les deux dernières années (catalogue) ; fichier modifié le 16/11/2026. |
| Clés | `NUM_POSTE` (8 chiffres, dont le département) + `AAAAMMJJ`. |
| Licence | Licence Ouverte 2.0 selon data.gouv.fr ; pas de mention dans le fichier. |
| Millésime | Période 2025-2026 inspectée. |
| Référentiel géographique | Coordonnées (LAT, LON) et altitude du poste. |
| Données personnelles | Aucune (le nom du poste est un lieu). |
| Questions servies | Q1 et Q3, **indirectement** (matière première d'un IFM recalculé). |
| Premiers constats qualité | Pas d'indice de danger : il faudrait recalculer l'IFM (température, humidité et vent à midi, pluie sur 24 h, initialisation des codes d'humidité en début de saison). Vent moyen (FFM) renseigné pour 47,6 % des lignes. |
| Décision | **Écartée** : recalcul lourd, vent manquant pour la moitié des stations, FWI CEMS (fiche 02) déjà calculé selon la même méthode. À reconsidérer si le FWI CEMS cesse d'être mis à jour (O06). |
