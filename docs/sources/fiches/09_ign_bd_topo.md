# Fiche 09 — BD TOPO® v3.5, IGN (Gironde) : bâtiments et zones de végétation

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | IGN. |
| Accès (URL) | https://www.data.gouv.fr/datasets/bd-topo-r ; éditions : `https://data.geopf.fr/telechargement/resource/BDTOPO?zone=D033` ; archive `BDTOPO_3-5_TOUSTHEMES_GPKG_LAMB93_D033_2026-09-15.7z`. Public, sans compte. |
| Contenu | 7z de 602 Mo → GeoPackage de 3,6 Go, plus de 40 couches. `batiment` : 1 446 771 bâtiments (`cleabs` unique), `usage_1` (résidentiel 557 037, indifférencié 691 760, annexe, commercial, agricole…), `nombre_de_logements`, `etat_de_l_objet` (1 446 046 en service). `zone_de_vegetation` : 240 957 polygones, `nature` (forêt fermée de conifères 455 744 ha, de feuillus 155 509 ha, mixte 52 790 ha, lande ligneuse 26 311 ha, forêt ouverte, bois, haie, vigne…). SHA-256 : `873ae563654ba5ee…`. Couverture : Gironde, avec une **marge sur les départements voisins** : 121 870 bâtiments en Charente-Maritime, Dordogne, Lot-et-Garonne et Landes (DQ10). |
| Granularité | Objet (bâtiment, polygone de végétation) ; aucun code commune sur les bâtiments (rattachement spatial). |
| Historique | Éditions trimestrielles (15/12/2025, 15/03/2026, 15/06/2026, 15/09/2026). Végétation : `date_modification` en 2024 pour 24 379 objets, 2020 pour 13 624, 2013-2014 pour 18 094, **vide pour 182 390**. Reclassement des surfaces brûlées en 2022 : `non vérifié`. |
| Fraîcheur | Trimestrielle pour le produit, inégale selon les objets. |
| Clés | `cleabs` (identifiant IGN). |
| Licence | Licence Ouverte 2.0 selon data.gouv.fr ; `non vérifiée` dans le fichier (LISEZ-MOI générique). |
| Millésime | Édition du **15/09/2026**. |
| Référentiel géographique | Lambert 93. |
| Données personnelles | Ni nom ni adresse dans `batiment`. **Indirectement personnel** : géométrie d'un bâtiment résidentiel isolé + `nombre_de_logements` désignent un foyer ; `adresse_ban` et `appariement_fichiers_fonciers` mèneraient au propriétaire : non chargés. |
| Questions servies | Q4 (bâti au contact de la végétation inflammable ; surface de végétation inflammable par commune, plus récente que la BD Forêt). |
| Premiers constats qualité | Le « bâti au contact de la forêt » dépend de la définition (1 446 046 bâtiments en service, 200 m au centroïde) : tout boisé → 1 424 321 (98 %) ; conifères + landes ligneuses + forêt mixte → 506 266 (35 %) ; mêmes essences en polygones ≥ 10 ha → 246 892 (17 %) ; ≥ 100 ha → 136 443 (9 %). Calcul indexé validé sur 2 000 bâtiments tirés au hasard (181 / 2 000 dans les deux cas). Ces chiffres portent sur toute la livraison, marge comprise. **Gironde seule** (1 323 816 bâtiments en service), conifères, forêt mixte, landes ligneuses en polygones ≥ 100 ha, 200 m : **122 235 bâtiments (9,2 %)**. |
| Décision | **Retenue** : seule source du bâti et de la végétation inflammable récente (Q4). |
