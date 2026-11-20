# Minimisation des données (RGPD, art. 5.1.c et 25)

Un champ n'entre dans le modèle que s'il sert une question (Q1-Q4) ou une jointure indispensable. Une donnée **pseudonymisée reste personnelle** (RGPD art. 4.5, considérant 26 ; CEPD, lignes directrices 01/2025).

## Couches concernées

| Couche | Contenu | Justification |
|---|---|---|
| `data/raw/` (fichiers) | Fichier **tel quel**, avec sa provenance | Intégrité et preuve d'origine (exigée par les mentions légales BDIFF, O04) ; idempotence par empreinte. Accès restreint, non diffusé, non commité. |
| `raw.*` (DuckDB) | Copie fidèle des colonnes du fichier, en texte | Traçabilité vers la source ; même statut que les fichiers. BD TOPO : seules les couches et colonnes utiles sont chargées. |
| `staging` et au-delà | **Uniquement les champs « garder »** | Première couche lisible par les analystes. |
| `marts` | Agrégats ou faits sans attribut personnel | Vus par le tableau de bord et la direction. |

Conservation : fichiers bruts supprimés par `rm -rf data/raw` à la fin du module (`make clean` les garde volontairement pour rejouer).

## Champ / question / décision

Colonne « Perso. » : **non** ; **indirect** (peut contribuer à identifier une personne par recoupement) ; **oui**.

### BDIFF

| Champ source | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| Année | Q2 | non | garder | Partie de l'identifiant du feu. |
| Numéro | jointure (identifiant) | indirect | garder en staging et intermédiaire ; **non exposé dans les marts** (clé de substitution) | Remonter à la fiche source, appliquer les règles de survivance ; renvoie à une fiche publique du portail BDIFF, donc le pseudonymiser n'enlèverait aucun risque. |
| Département | Q1-Q3 | non | garder | Filtre d'emprise, cohérence avec le code commune. |
| Code INSEE | Q1, Q3, Q4 | indirect | garder | Clé de jointure territoire ; seul, ne désigne personne. |
| Nom de la commune | — | non | **écarter** | Libellé variable (373 pour 369 codes) ; libellé repris du COG. |
| Date de première alerte : **date** | Q1, Q2, Q3 | indirect | garder | Grain jour des questions. |
| Date de première alerte : **heure et minute** | — | **indirect** | **écarter** (généraliser à la date) | Aucune question sous le jour (Q3 compte les feux du même jour) ; commune + date + heure + cause + presse locale → auteur présumé dans un petit village. |
| Surface parcourue | Q3, KPI surface moyenne | non | garder (en ha) | Mesure centrale de Q3. |
| Surface forêt et autres composantes (8 colonnes) | — | non | **écarter** | Aucune décision ne les utilise ; double comptage (DQ04). |
| Précision des surfaces | — | non | **écarter** | Vide à 89 % avant 2023 ; aucun calcul (QT2). |
| Type de peuplement, Maquis-garrigues | — | non | **écarter** | Vides hors zone méditerranéenne. |
| Nature (cause) | — | **indirect** | **écarter** | Aucune décision n'en dépend ; « Malveillance » ou « Involontaire (particulier) » + commune + date désigne une personne : ré-identification, stigmatisation, données d'infraction (RGPD art. 10). |
| Décès ou bâtiments touchés, nombre de décès, bâtiments détruits | — | **oui** (victimes, propriétaires) | **écarter** | Aucune question ; personnes identifiables dans une petite commune ; toujours 0 dans l'extraction. |
| Précision de la donnée | qualité Q3 | non | garder (indicateur `donnee_partielle`) | Exclure ou signaler les 10 fiches « partielles ou non valides » dans le calcul du seuil. |

### Météo des forêts

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| date (émission) | Q1, Q3 | non | garder (dériver la date cible J+1 / J+2) | Grain jour. |
| num_dep | Q1, Q3 | non | garder (normalisé sur 2 caractères) | Jointure. |
| niveau_j1 | Q1, Q3 | non | garder | Prévision du lendemain. |
| niveau_j2 | Q3 | non | garder | Une demande de renforts demande du délai : le surlendemain est utile. |
| nom_dep / dep_nom | — | non | **écarter** | Libellé (repris du COG). |

### FWI CEMS

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| valid_time, latitude, longitude | Q1, Q3 | non | garder | Clé (jour, maille). |
| fwinx | Q1, Q3 | non | garder | Indice de danger. |
| 13 autres indices (BUI, ISI, KBDI…) | — | non | **non demandés** à l'API | Minimisation dès la collecte. |

### COG INSEE

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| COM, TYPECOM, DEP, REG | toutes (territoire) | non | garder | Clés et hiérarchie. |
| LIBELLE | affichage | non | garder | Libellé officiel unique pour tous les marts. |
| TNCC, NCC, NCCENR | — | non | **écarter** | Variantes typographiques du libellé. |
| ARR, CAN, CTCD, COMPARENT | — | non | **écarter** | Aucune question à ces niveaux ; le secteur opérationnel du SDIS n'est pas l'arrondissement (M8). |
| DATE_DEBUT, DATE_FIN (historique) | SCD2 | non | garder | Validité des versions de commune. |
| MOD, DATE_EFF, COM_AV, COM_AP, TYPECOM_AV/AP (mouvements) | SCD2 | non | garder | Rattacher un code disparu à son successeur. |
| Libellés avant / après des mouvements | — | non | **écarter** | Redondants avec l'historique code-libellé. |

### ADMIN EXPRESS COG CARTO

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| code_insee, géométrie | Q1 (centroïde → maille), Q4 (rattachement spatial) | non | garder | Jointures spatiales. |
| population, date_du_recensement | — | non | **écarter** | Recopie de la population INSEE (D16). |
| nom, statut, codes SIREN, EPCI, code postal, superficie cadastrale… | — | non | **écarter** | Aucune question. |

### BD TOPO

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| batiment.cleabs | jointure, unicité | indirect | garder (intermédiaire seulement) | Identifiant technique. |
| batiment.géométrie → **centroïde** | Q4 | **indirect** (un point = un foyer) | garder **le centroïde seulement**, en intermédiaire ; **agrégé à la commune dans les marts** | La forme exacte n'apporte rien à une distance de 200 m ; aucun bâtiment individuel publié. |
| batiment.usage_1 | Q4 | non | garder | Distinguer résidentiel, annexes, activités. |
| batiment.etat_de_l_objet | Q4 (filtre) | non | filtre au chargement (« En service »), non stocké | |
| batiment.nombre_de_logements | — | indirect | **écarter** | Vide à 52 % (QT4) ; on compte des bâtiments. |
| batiment.adresses, identifiants RNB, appariement fichiers fonciers, sources | — | **indirect → propriétaire** | **écarter (non chargés)** | Remonteraient au propriétaire via les fichiers fonciers. |
| batiment.hauteur, matériaux, altitudes, précisions… | — | non | **écarter** | Aucune question. |
| zone_de_vegetation.cleabs, nature, géométrie | Q4 | non | garder | Surface inflammable, distance au bâti. |
| zone_de_vegetation.date_modification | qualité Q4 | non | garder | Signaler l'âge de la donnée (M6). |
| Autres couches (adresse_ban, routes, ERP…) | — | indirect (adresses) | **non chargées** | Aucune question. Les ERP (campings) seraient utiles à Q4 en v2, à justifier alors. |

### Capacités d'hébergement touristique

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| GEO, GEO_OBJECT | Q4 | non | garder (filtre `COM`, 33) | Clé commune. |
| ACTIVITY, TOUR_MEASURE, L_STAY | Q4 | non | garder | Type d'hébergement et mesure. |
| UNIT_LOC_RANKING | — | indirect (hôtel 5 étoiles unique dans la commune = un établissement) | **filtrer sur `_T`**, détail par classement non gardé | N'éclaire pas la protection ; ferait ressortir des établissements uniques. |
| TIME_PERIOD, OBS_VALUE | Q4 | non | garder | Millésime et valeur. |
| FREQ, OBS_STATUS | — | non | **écarter** | Constants. |

### Populations légales

| Champ | Question | Perso. | Décision | Justification |
|---|---|---|---|---|
| COM, DEP | Q4 | non | garder | Clé. |
| PMUN | Q4 | non | garder | Population résidente (semi-additive). |
| PTOT | Q4 | non | garder | Population totale (inclut les personnes comptées à part : internats, casernes…). |
| PCAP | — | non | **écarter** | Se déduit (PTOT − PMUN). |
| Noms, codes arrondissement / canton | — | non | **écarter** | Libellés et niveaux non utilisés. |

## Risques de ré-identification par croisement

| Croisement | Risque | Mesure |
|---|---|---|
| BDIFF (commune + date + heure + cause) × presse locale | Désigner l'auteur présumé ou la victime d'un feu dans un petit village | Heure et cause écartées dès le staging. |
| BDIFF (commune + date + surface) × presse | Un feu daté dans une commune est un **événement public** ; sans cause ni heure, il ne désigne personne | Accepté. |
| BD TOPO (point d'un bâtiment) × fichiers fonciers / adresses | Remonter au propriétaire d'une habitation « au contact de la forêt » | Adresses et liens fonciers non chargés ; points en intermédiaire seulement ; marts agrégés à la commune. |
| Hébergement (classement) × annuaire touristique | Isoler un établissement | Seuls les totaux `_T` gardés. |
| Données internes SDIS (si collectées, M5) | Noms d'agents, adresses d'intervention, victimes | Pseudonymisation **à la source** (table de correspondance gardée par le SDIS) ; restent personnelles : base légale, durée de conservation et analyse d'impact à prévoir avant collecte. |
