# Fiche 11 — Populations légales 2023 (en vigueur au 01/01/2026), INSEE

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | INSEE (recensement de la population). |
| Accès (URL) | https://www.insee.fr/fr/statistiques/8680726 → `/fr/statistiques/fichier/8680726/ensemble.zip`. Public, sans compte. |
| Contenu | Zip (1 Mo) → 8 CSV (`;`) par niveau géographique + `metadonnees.csv`, datés du 10/12/2025. `donnees_communes.csv` : région, département, arrondissement, canton, code et nom de commune, **PMUN** (municipale), **PCAP** (comptée à part), **PTOT** (totale). Gironde : 534 communes, PMUN 1 690 493, PTOT 1 716 986 ; Landes : 327 communes, PMUN 433 570. SHA-256 : `5174fc225398a4c0…`. |
| Granularité | Commune × millésime de recensement. |
| Historique | Un fichier par millésime (`non vérifié` pour les années antérieures : non téléchargées). |
| Fraîcheur | Annuelle (fin décembre). |
| Clés | `COM`. |
| Licence | Licence Ouverte 2.0 selon les conditions de réutilisation d'insee.fr ; pas de mention dans le fichier. |
| Millésime | Recensement 2023, en vigueur au 01/01/2026. |
| Référentiel géographique | Géographie au 01/01/2025 ou 2026 : `non vérifié` dans le fichier ; les 861 codes 33 + 40 correspondent exactement à ADMIN EXPRESS 2026. |
| Données personnelles | Aucune (agrégats communaux). |
| Questions servies | Q4 (population résidente exposée). |
| Premiers constats qualité | PMUN identique à `population` d'ADMIN EXPRESS pour les 861 communes. PMUN est la population **résidente** : touristes exclus. |
| Décision | **Retenue** : population résidente (Q4). |
