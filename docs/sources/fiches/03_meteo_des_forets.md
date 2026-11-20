# Fiche 03 — Météo des forêts (archives), Météo-France

Fichiers ouverts le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | Météo-France. |
| Accès (URL) | https://www.data.gouv.fr/datasets/archives-de-la-meteo-des-forets ; `https://meteofrance.s3.sbg.io.cloud.ovh.net/data/BULLETIN/MDF/mdf_<année>.csv.gz` (2024, 2025, 2026). Trouvée par recherche « météo des forêts » sur data.gouv.fr. Public, sans compte. |
| Contenu | Par bulletin (émis vers 16h-17h UTC), niveau de danger **prévu à J+1 et J+2** par département : 1 faible, 2 modéré, 3 élevé, 4 très élevé. CSV gzip, **trois schémas** : 2024 `date,num_dep,niveau_j1,niveau_j2,nom_dep` ; 2025 colonne `dep_nom` ; 2026 séparateur `;`. 35 616 lignes, 40 à 50 Ko par an. SHA-256 : 2024 `e3f87c1161d30491…`, 2025 `dd0a095b1744ef7c…`, 2026 `c02f4f539370a663…`. |
| Granularité | **Département × date d'émission** ; pas de zone infra-départementale. |
| Historique | Depuis le 03/06/2024 (dispositif né en 2023, 2023 non publié). **Saisonnier** : 2024 et 2025 du 03/06 au 30/09, 2026 du 28/05 au 05/10 ; or 30 % des feux de Gironde 2006-2025 (1 052 sur 3 555) partent entre janvier et mai. 96 départements. |
| Fraîcheur | Fichier 2026 modifié le 05/10/2026 (`Last-Modified`) : mise à jour en fin de saison. |
| Clés | `num_dep` + date d'émission. |
| Licence | Licence Ouverte 2.0 selon data.gouv.fr ; `non vérifié` dans le fichier (aucune mention). |
| Millésime | Saisons 2024, 2025, 2026. |
| Référentiel géographique | Code département, sans zéro à gauche en 2024-2025 (`1`), avec en 2026 (`01`). |
| Données personnelles | Aucune. |
| Questions servies | Q1 (seule **prévision J+1** ouverte constatée), Q3 (niveau prévu la veille). |
| Premiers constats qualité | Gironde 2026 plus sévère (61 jours en niveau 2 et 14 en niveau 3 à J+1, contre 13 et 1 en 2024) ; niveau 3 du 20 au 23/07/2026. Le niveau intègre l'occupation du sol et les zones sensibles : pas un indice météo pur. |
| Décision | **Retenue** : seule prévision J+1, malgré le grain départemental et la saison seule. |
