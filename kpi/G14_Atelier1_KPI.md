# G14 — Atelier 1 : de la décision au premier chiffre

Projet feux de forêt · Gironde · séance du 19 novembre 2026

## A. Décision

| Composante | Choix |
|---|---|
| Décideur | Directeur du SDIS 33 |
| Décision | Date de début du renfort des sapeurs-pompiers saisonniers |
| Options | A : juillet-août (actuel) · B : dès le 1er juin · C : dès le 15 juin |
| Périmètre | Gironde, par mois (Landes en comparaison) |
| Horizon | Saison 2027, décision au printemps 2027 |

**Question.** Pour la saison 2027, le SDIS 33 doit-il avancer le renfort de ses saisonniers au 1er juin, au 15 juin, ou le garder sur juillet-août ?

**Objectif du défi : outillage des pompiers.** La question porte sur le calendrier des moyens de lutte. Elle reprend la question Q2 du dossier de sources. « Juillet-août » désigne la période actuelle du renfort ; le mot « été », ambigu, est évité.

## B. Indicateurs candidats

| # | Indicateur | Maillon | Amont / aval | Levier / contexte | Verdict |
|---|---|---|---|---|---|
| 1 | Effectif saisonnier présent en juin | Moyens | Amont | Levier | Gardé · Easy : non public |
| 2 | Délai d'arrivée sur feu en juin | Réalisations | Aval | Levier | Gardé · Easy : non public |
| 3 | K1 : départs par jour, juin ÷ juillet-août | Besoin | Amont | Contexte | Gardé · Robust : 2024 incomplète |
| 4 | K2 : surface brûlée par jour, juin ÷ juillet-août | Résultats | Aval | Levier | Gardé · Robust : un grand feu pèse tout |
| 5 | K4 : part des feux > 1 ha, juin vs juillet-août | Résultats | Aval | Levier | Gardé · Accepted : seuil de 1 ha |
| 6 | Bâtiments détruits par les feux de juin | Impacts | Aval | Levier | Gardé · Robust : cas très rares |
| 7 | K3 : jours de danger élevé, juin ÷ juillet-août | Besoin | Amont | Contexte | Gardé · Credible : maille de 25 km |
| 8 | Date du 10e départ de l'année | Besoin | Amont | Contexte | Gardé · Credible : recule si les feux baissent |
| ~~9~~ | ~~Nombre de feux par an~~ | — | — | — | Barré : ne dit pas quand ils surviennent |
| ~~10~~ | ~~Causes des feux de juin~~ | — | — | — | Barré : prévention hors SDIS, risque RGPD |

## C. GQM et arbre

**Objectif.** Caler le renfort saisonnier sur la période réelle d'activité des feux.

- G1. Juin a-t-il une activité comparable à juillet-août ? → 3, 8
- G2. Les feux de juin s'aggravent-ils faute de moyens ? → 4, 5, 6, 1, 2
- G3. Le danger de juin se rapproche-t-il de juillet-août ? → 7

**Arbre de KPIs**

- K1 (décision)

**Équations.** Exacte : K2 = K1 × (surface moyenne par feu en juin ÷ surface moyenne par feu en juillet-août). Approchée : départs de juin ≈ jours de danger élevé × départs par jour de danger élevé.

**Options.** B et C agissent sur la surface moyenne par feu (K2, K4) ; aucune n'agit sur K1. A est la référence.

## D. Fiches KPI

| Champ | K1 · décision | K2 · pilotage | K4 · pilotage |
|---|---|---|---|
| Question | Juin a-t-il une activité comparable à juillet-août ? | Les feux de juin font-ils autant de dégâts ? | L'attaque initiale de juin garde-t-elle les feux petits ? |
| Formule | (départs juin ÷ 30) ÷ (départs juillet-août ÷ 62) × 100 | (surface juin ÷ 30) ÷ (surface juillet-août ÷ 62) × 100 | Part des feux > 1 ha en juin − même part en juillet-août |
| Unité | % | % | points |
| Paramètres | Mois, période, territoire | Idem + exclusion des feux > 1 000 ha | Seuil de 1 ha |
| Périmètre | Gironde · 2021-2025 · mois × année · annuel | Idem | Idem |
| Proxy et biais | Mesure le besoin par les départs, pas par la charge : surestime un peu juin | Un grand feu compté le jour de son départ ; Landiras (juillet 2022) sous-estime juin | Le vent et la sécheresse jouent autant que les moyens |
| Décision | Élevé : B · intermédiaire : C · faible : A | En hausse : renforce B | Positif : renforce B |
| Propriétaire | Le groupe | Le groupe | Le groupe |
| Valeur actuelle | Partie E | 8,4 % (médiane 2021-2025 ; 23,0 % hors feux > 1 000 ha) | −15,0 points (médiane 2021-2025) |

**Sources.** [BDIFF](https://bdiff.agriculture.gouv.fr/incendies), ministère de l'Agriculture (site IGN) : Année, Numéro, Code INSEE, Date de première alerte, Surface parcourue (m²). [Code officiel géographique 2026](https://www.insee.fr/fr/information/2560452), Insee : v_commune_2026 (COM, DEP), v_mvt_commune_2026 (MOD, DATE_EFF, COM_AV, COM_AP).

**Faisabilité.** BDIFF ouverte le 17/11/2026 : 2006-2025, commune de départ, 3 555 feux en Gironde, aucune surface nulle ; 20 codes de commune disparus, rattachés par le COG ; 2024 : 29 feux contre 103 à 245 les années voisines (règle de qualité QR08).

## E. Calcul du KPI de décision

| Consolidation | Valeur |
|---|---|
| Sources jointes | BDIFF + COG Insee |
| Clé et maille | Code INSEE rapporté à la commune 2026 · mois × année, Gironde |
| Lignes 2021-2025 | 571 |
| Lignes perdues à la jointure | 0 (motif : aucun ; 1 feu de 2022 au code disparu 33409 rattaché à 33008 Porte-de-Benauge par les mouvements du COG) |

| Année | Départs en juin (brut) | Base : départs par jour en juillet-août | K1 (%) |
|---|---|---|---|
| 2021 | 2 | 0,19 | 34,4 |
| 2022 | 23 | 2,39 | 32,1 |
| 2023 | 17 | 0,50 | 113,3 |
| 2024 | 4 | 0,31 | 43,5 |
| 2025 | 11 | 1,40 | 26,1 |
| Moyenne | 11,4 | 0,96 | 49,9 |
| Médiane | 11 | 0,50 | 34,4 |

Part des départs de juin due à l'année la plus forte : 40,4 % (2022, 23 départs sur 57).

| Test de sensibilité | K1 médian (%) | Conclusion |
|---|---|---|
| Référence | 34,4 | Un jour de juin compte environ un tiers des départs d'un jour de juillet-août |
| Sans 2024 | 33,3 | −1,2 point : l'année 2024 incomplète ne déplace pas la médiane |
| Gironde et Landes | 45,2 | +10,8 points : la valeur dépend du territoire, mais reste sous 50 % |

**Lecture.** Le chiffre brut aurait fait conclure que juin a le plus pesé en 2022 (23 départs, 40,4 % des départs de juin 2021-2025). Le chiffre normalisé montre qu'en 2022 un jour de juin ne compte que 32,1 % des départs d'un jour de juillet-août, et qu'en médiane il en compte 34,4 % ; seule 2023 dépasse 100 % (113,3 %), ce qui tire la moyenne à 49,9 %. Cette lecture résiste au test, car le K1 médian reste à 33,3 % sans 2024 et monte à 45,2 % avec les Landes, toujours sous la moitié de l'activité journalière de juillet-août.

## F. Effet pervers

Les feux de la BDIFF sont saisis en partie par les services de secours eux-mêmes. Si K1 décide du nombre de saisonniers, celui qui saisit les feux a intérêt à en déclarer davantage en juin (pour obtenir des renforts) ou moins (pour réduire la dépense) : le chiffre bouge sans que la réalité change.

**Parade :** fixer la règle de décision avant de voir les chiffres, l'appliquer à la médiane de 5 ans (une année gonflée pèse peu), et revérifier chaque année un échantillon de fiches BDIFF de juin.
