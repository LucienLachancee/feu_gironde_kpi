# Fiche 08 — BD Forêt® V2, IGN (Gironde)

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | IGN. |
| Accès (URL) | https://www.data.gouv.fr/datasets/bd-foret-r ; éditions : `https://data.geopf.fr/telechargement/resource/BDFORET?zone=D033` ; archive `BDFORET_2-0__SHP_LAMB93_D033_2017-05-10.7z` (page geoservices.ign.fr rendue en JavaScript : passage par l'API Atom de la Géoplateforme). Public, sans compte. |
| Contenu | 7z (43 Mo) → shapefile `FORMATION_VEGETALE`, métadonnées XML, synthèse PDF. 53 130 polygones ; `CODE_TFV` / `TFV` (32 postes), `TFV_G11` (11 groupes), `ESSENCE`. Gironde : 549 745 ha cartographiés, dont 222 194 ha de pin maritime pur, 122 867 ha de « forêt fermée sans couvert arboré », 21 060 ha de landes. SHA-256 : `17179c5b2878f05f…`. |
| Granularité | Polygone de végétation ≥ 0,5 ha. |
| Historique | Une V1 (2013-01-01, nomenclature départementale, non comparable). Landes : V2 du 01/10/2018 `non ouverte` (emprise Q4 limitée à la Gironde). |
| Fraîcheur | **Aucune mise à jour depuis 2009** en Gironde : ignore les feux de 2022 (près de 29 000 ha selon la BDIFF), la tempête Klaus (janvier 2009 ; position par rapport aux prises de vue `non vérifiée`) et Saumos 2026. |
| Clés | `ID` (polygone) ; aucun code commune (rattachement spatial). |
| Licence | Licence Ouverte 2.0 selon data.gouv.fr ; `non vérifiée` dans le fichier (LISEZ-MOI générique). |
| Millésime | Photographies **2009** ; diffusion 2013 ; édition 2017-05-10 ; métadonnées 2022-09-14. |
| Référentiel géographique | Lambert 93. |
| Données personnelles | Aucune. |
| Questions servies | Q4 (surface de végétation inflammable par commune). |
| Premiers constats qualité | 8 géométries invalides ; libellés `TFV` en cp1252 lus comme UTF-8 (`d\x92un`) : usage de `CODE_TFV` ; millésime 2009. |
| Décision | **Écartée** : millésime 2009 ; la couche `zone_de_vegetation` de la BD TOPO 2026 est plus récente et distingue conifères, feuillus, mixte et landes ligneuses. Perte faible : 222 194 ha de pin maritime pur sur 223 346 ha de forêt fermée de conifères. |
