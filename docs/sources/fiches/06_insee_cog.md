# Fiche 06 — Code officiel géographique (COG) et historique des communes, INSEE

Fichiers ouverts le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | INSEE. |
| Accès (URL) | https://www.insee.fr/fr/information/2560452 → millésime 2026 : https://www.insee.fr/fr/information/8740222 ; fichiers `v_commune_2026.csv`, `v_commune_depuis_1943.csv`, `v_mvt_commune_2026.csv`, `v_departement_2026.csv` (`/fr/statistiques/fichier/8740222/…`). Public, sans compte. |
| Contenu | CSV UTF-8, `,`, champs entre guillemets. `v_commune_2026` : communes au 01/01/2026 (COM, COMA, COMD, ARM) avec département, région, arrondissement, canton. `v_commune_depuis_1943` : chaque couple code-libellé avec `DATE_DEBUT`, `DATE_FIN`. `v_mvt_commune_2026` : événements (fusion, changement de nom, rétablissement…) avec code avant / après et date d'effet. 3 Mo + 3 Mo + 1 Mo. SHA-256 : communes 2026 `7be1153de3a63df4…`, depuis 1943 `08c532ed8dade0a0…`, mouvements `8b339fad8232e972…`. |
| Granularité | Commune ; commune × période (historique) ; événement (mouvements). |
| Historique | 42 288 périodes pour 39 117 codes, 1943-2026 ; 13 734 événements du 19/02/1943 au 01/01/2026, dont 119 en Gironde ou Landes. |
| Fraîcheur | Annuelle (au 1er janvier) ; page mise à jour le 24/02/2026. Aucune commune nouvelle entre 2025 et 2026. |
| Clés | `COM` ; `(COM, DATE_DEBUT)` ; `(MOD, DATE_EFF, COM_AV, COM_AP)`. |
| Licence | Licence Ouverte 2.0 selon les pages INSEE / data.gouv.fr ; pas de mention dans les CSV. |
| Millésime | COG 2026 : 34 875 communes, dont 534 en Gironde et 327 dans les Landes. |
| Référentiel géographique | C'est le référentiel. Tous les codes BDIFF se rattachent à une période valide à leur date de feu ; 33 feux ne se rattachent pas au COG 2026 (fusions 2016-2025 : Val de Virvée, Margaux-Cantenac, Porte-de-Benauge, Val-de-Livenne, Blaignan-Prignac…). |
| Données personnelles | Aucune. |
| Questions servies | Toutes : dimension territoire historisée (SCD2), rattachement de chaque feu à la commune en vigueur à sa date. |
| Premiers constats qualité | `v_commune_depuis_1943` décrit des couples code-libellé : un changement de nom crée une période (ex. Cadillac → Cadillac-sur-Garonne en 2023). Le rattachement d'un code disparu à une commune actuelle exige les mouvements (MOD 32 = fusion, commune nouvelle). |
| Décision | **Retenue** : indispensable aux jointures (feu de 2013 → commune de 2013). |
