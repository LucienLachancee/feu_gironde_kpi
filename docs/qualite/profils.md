# Profils de qualité des sources retenues

Profilage du 17/11/2026 avec DuckDB 1.4.5, sur les fichiers des fiches sources (mêmes empreintes SHA-256). Qualité jugée pour l'usage (Q1 à Q4). Deux complétudes distinguées :

- **valeurs vides** : champ non renseigné dans une ligne qui existe ;
- **territoires ou périodes absents** : lignes inexistantes, révélées par un référentiel externe (COG, calendrier, grille).

Défaillances et décisions faussées : [`defaillances.md`](defaillances.md) ; règles et seuils : [`regles_qualite.md`](regles_qualite.md).

## 1. BDIFF (Gironde + Landes, 2006-2025) — 5 460 feux

**Valeurs vides, bornes, distinctes**

| Champ | Remplissage | Bornes / distinctes | Remarque |
|---|---|---|---|
| Année, Numéro | 100 % | 2006-2025 ; `(Année, Numéro)` unique | `Numéro` seul n'est pas unique |
| Département | 100 % | 33, 40 | |
| Code INSEE | 100 % | 369 codes en Gironde | tous valides à la date du feu ; 33 absents du COG 2026 |
| Nom de la commune | 100 % | 373 libellés pour 369 codes (Gironde) | libellés variables : aucune jointure dessus |
| Date de première alerte | 100 % | 05/02/2006 → 28/12/2025 ; année = année de la date pour 100 % | 2,1 % des heures à la minute 00 (pas de troncature massive) |
| Surface parcourue (m²) | 100 % | 1 m² → 12 552 ha ; médiane 0,1 ha ; 979 feux < 0,01 ha | aucun zéro |
| Surface forêt (m²) | 100 % | jamais supérieure au total | |
| Composantes de surface | variable (formulaire avant / après 2023) | **4 feux** dont la somme des composantes vaut exactement **2 × le total** | double saisie (Callen 2017 : 491,6 ha comptés deux fois) |
| Précision des surfaces | 11,2 % avant 2023, **100 %** depuis 2023 | Estimées / Mesurées | changement de formulaire |
| Nature (cause) | **44,8 %** (2006-2015), **42,5 %** (2016-2025) | 5 modalités | remplissage stable selon la taille du feu (42 à 50 %) ; mécanisme (MCAR / MAR / MNAR, Rubin 1976) `non vérifié` |
| Type de peuplement, Maquis-garrigues | 0 % | — | normal hors zone méditerranéenne |
| Décès, bâtiments détruits | 3,4 % | toujours 0 | |

**Périodes absentes** (référentiel : calendrier des campagnes)

| Année | Gironde | Landes | | Année | Gironde | Landes |
|---|---|---|---|---|---|---|
| 2006 | 383 | 219 | | 2016 | 200 | 113 |
| 2007 | 106 | 62 | | 2017 | 181 | 72 |
| 2008 | 129 | 92 | | 2018 | 122 | 38 |
| 2009 | 266 | 172 | | 2019 | 161 | 59 |
| 2010 | 356 | 145 | | 2020 | 145 | 76 |
| 2011 | 314 | 133 | | 2021 | 65 | 52 |
| 2012 | 192 | 91 | | 2022 | 245 | 128 |
| 2013 | 79 | 42 | | 2023 | 103 | 84 |
| 2014 | 122 | 55 | | **2024** | **29** | **30** |
| 2015 | 228 | 131 | | 2025 | 129 | 111 |

- **2024** très bas dans les deux départements : année calme ou saisie incomplète, `non vérifié` (la baisse simultanée dans deux départements saisis par des services différents plaide pour une année calme, sans le prouver).
- **2026 absent** (Saumos).

**Territoires absents** (référentiel : COG 2026) : 171 des 534 communes de Gironde n'ont aucun feu en 20 ans. Pas un manque : une commune sans feu est un zéro, à faire apparaître par un fait commune × jour complété par le référentiel.

**Unicité et doublons**

| Contrôle | Résultat |
|---|---|
| Couples (commune, horodatage) à deux fiches | 37 : 33 à surfaces différentes (départs multiples plausibles), **4 à même surface** (doublons possibles) |
| Couples (commune, jour) à plusieurs feux | 236 (523 feux) |
| Pic de départs | 58 le 27/07/2006 (31 en Gironde, 27 dans les Landes) |
| Grands feux (≥ 100 ha) | 26 en 20 ans (15 en Gironde, 11 dans les Landes), dont 9 en 2022 : échantillon **petit** pour estimer un seuil (Q3) |

## 2. Météo des forêts (2024-2026) — 35 616 bulletins départementaux

| Contrôle | Résultat |
|---|---|
| Niveaux J+1 et J+2 dans {1, 2, 3, 4} | 100 % (aucune valeur vide) |
| Unicité (département, date d'émission) | 100 % |
| Codes département | 105 valeurs brutes → **96 après complétion à 2 caractères** (`1` → `01`) |
| Schéma | 3 schémas (colonne `nom_dep` / `dep_nom`, séparateur `,` / `;`) |
| Jours manquants en saison (Gironde ; référentiel : calendrier du premier au dernier bulletin de chaque année) | **0** |
| Cohérence J+1 du jour J et J+2 de la veille (Gironde) | identiques 345 fois sur 368, jamais plus d'un niveau d'écart |
| Période absente | hors saison (couverture au mieux 28/05 → 05/10) : **aucune prévision**, alors que 30 % des feux de Gironde partent entre janvier et mai |
| Distribution Gironde J+1 (niveaux 1/2/3/4) | 2024 : 106 / 13 / 1 / 0 ; 2025 : 79 / 37 / 4 / 0 ; 2026 : 56 / 61 / 14 / 0 |

## 3. FWI CEMS (réanalyse) — fichier test juillet 2022

| Contrôle | Résultat |
|---|---|
| Volume | 31 jours × 99 mailles |
| Valeurs manquantes | 0 |
| Bornes FWI | 0,06 → 77,4 |
| Mailles marines | présentes (valeurs calculées sur la mer) : exclues par le rattachement aux communes |
| Fraîcheur | mises à jour suspendues depuis le 16/11/2026 (O06) |

## 4. COG INSEE

| Contrôle | Résultat |
|---|---|
| Périodes qui se chevauchent pour un même code (Gironde, Landes) | 0 |
| `DATE_FIN` < `DATE_DEBUT` | 0 |
| Codes avec plus d'une période ouverte | 0 |
| Rattachement des codes BDIFF à leur date | 100 % |

## 5. Capacités d'hébergement touristique 2026

| Contrôle | Résultat |
|---|---|
| Communes de Gironde et des Landes du COG 2026 absentes | 0 |
| Codes hors COG 2026 | 0 (géographie 2026 après le rechargement du 27/08/2026) |
| Valeurs négatives ou non entières | 0 |
| Total `_T` = somme des classements (campings) | 100 % cohérent |
| Total = de passage + à l'année (campings) | 100 % cohérent |
| Communes de Gironde sans hébergement marchand | 414 sur 534 (vrai zéro, pas un manque) |

## 6. Populations légales 2023

| Contrôle | Résultat |
|---|---|
| Communes du COG 2026 absentes | 0 |
| Somme des communes = total départemental | exact (Gironde 1 690 493 ; Landes 433 570) |
| PTOT < PMUN | 0 |
| Bornes Gironde | 41 → 267 991 habitants |

## 7. BD TOPO (Gironde) et ADMIN EXPRESS

| Contrôle | Résultat |
|---|---|
| `cleabs` unique (bâtiments) | 100 % |
| Bâtiments de la livraison D033 situés **hors de Gironde** | **121 870** (Charente-Maritime 42 713, Dordogne 36 986, Lot-et-Garonne 25 106, Landes 17 065) : marge de livraison |
| Bâtiments rattachés à aucune commune des 6 départements | 360 (bord de mer et estuaire, contours généralisés) |
| Bâtiments en service en Gironde | 1 323 816 |
| `nombre_de_logements` vide | 751 621 (52 %) ; 28 395 bâtiments résidentiels sans nombre de logements |
| Végétation : géométries invalides / nature vide | 0 / 0 |
| Végétation : `date_modification` vide | 182 390 sur 240 957 |
| Communes ADMIN EXPRESS : géométries invalides | 0 ; 534 communes = COG 2026 |
