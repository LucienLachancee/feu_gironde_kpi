# Analyse de la commande

Les questions ont été construites à partir du contexte décrit dans le cadrage du module (incendie de Saumos, juillet 2026). Commanditaire supposé : le **SDIS 33** (D01).

## 1. Périmètre de décision

| Décision | Qui la prend | Dans le périmètre ? |
|---|---|---|
| Surveillance, patrouilles, prépositionnement des groupes d'intervention feux de forêt (GIFF) | SDIS 33 (CODIS, direction) | **Oui** |
| Volume et calendrier des sapeurs-pompiers saisonniers | SDIS 33 (direction, avec le conseil d'administration qui vote le budget) | **Oui** |
| Demande de renforts extra-départementaux (colonnes, moyens aériens) | SDIS 33 la formule ; la zone de défense (COZ Sud-Ouest) et l'État l'arbitrent | **Oui** (la demande) |
| Conduite de la lutte, priorités de protection des points sensibles | Commandant des opérations de secours (SDIS) | **Oui** |
| Évacuations | Préfet (directeur des opérations) | Non (D02) |
| Contrôle des obligations légales de débroussaillement | Maires, préfet | Non (D02) |
| Aménagement forestier, pistes DFCI, points d'eau | Département, DFCI, ONF | Non (D02) |

## 2. Questions analytiques

| # | Question | Décision éclairée | Si X → A / si Y → B |
|---|---|---|---|
| Q1 | Demain, quelles zones de Gironde ont le danger de feu le plus élevé, d'après la météo prévue et l'historique des départs ? | Surveillance et prépositionnement quotidiens | Danger élevé → GIFF ou patrouille prépositionné dans la zone ; faible → moyens en caserne ou redéployés vers une zone plus exposée |
| Q2 | Sur quelles semaines se concentrent les départs de feu, et la saison commence-t-elle plus tôt qu'il y a dix ans ? | Calendrier et volume des saisonniers | Saison avancée (part croissante des départs en juin, 10ᵉ départ plus précoce) → recrutement et formation dès juin ; sinon → calendrier juillet-août |
| Q3 | À partir de quel niveau de danger et de combien de feux simultanés un départ devient-il un grand feu (seuil de 100 ha, hypothèse) ? | Demande anticipée de renforts extra-départementaux | Danger prévu et départs attendus au-dessus du seuil observé → renforts demandés la veille ; sinon → moyens propres du département |
| Q4 | Quelles zones combinent végétation inflammable et forte présence humaine (bâti au contact de la forêt, campings, population saisonnière) ? | Priorités de protection des points sensibles | Double enjeu → moyens de protection pré-affectés dans le plan de lutte ; sinon → stratégie d'attaque directe du feu |

## 3. Questions écartées

| Question | Raison |
|---|---|
| Quelles communes évacuer en priorité selon la progression du feu ? | Décision du préfet ; donnée en temps réel (front du feu) hors de portée d'un pipeline par lots. |
| Quelles parcelles ne respectent pas l'obligation de débroussaillement ? | Décision des maires ; croiser parcelles et propriétaires fait entrer des données personnelles sans finalité pour le SDIS. |
| Le feu de Saumos 2026 a-t-il brûlé les mêmes parcelles qu'en 2022 ? | Utile au retour d'expérience, mais ne mène à aucune décision du SDIS ; conservé comme contexte (EFFIS). |

## 4. Termes ambigus

| Terme | Interprétation retenue | Point non vérifié |
|---|---|---|
| « Feux importants » / « grand feu » | Surface finale > 100 ha (hypothèse, seuil paramétrable dans le modèle) | Seuil réellement utilisé par le SDIS 33 (100 ha ? 500 ha ? critère de moyens engagés ?) : aucune source consultée. |
| « Zone » (Q1) | Commune, ou maille de la grille météo | Maille réelle de prépositionnement (commune, massif, zone de la Météo des forêts, secteur de groupement). Le grain dépend de la source de danger disponible. |
| « Danger de feu » | Indice forêt météo (IFM, *Fire Weather Index* canadien) ou niveau de la Météo des forêts (faible → exceptionnel) | Indicateur utilisé par le CODIS ; si niveau qualitatif, table de passage IFM → niveau. |
| « Départ de feu » | Un enregistrement de la BDIFF : un feu, une commune, une date d'alerte | Saisie de tous les très petits feux ; comptage unique d'un feu sur plusieurs communes. |
| « Feux simultanés » | Nombre de départs le même jour dans le département | Même jour calendaire ou même créneau de quelques heures ; Gironde seule ou Gironde + Landes. |
| « Saison » / « plus tôt » | Distribution des départs par semaine ISO ; date du 10ᵉ départ de l'année | Unité de raisonnement du SDIS (semaines, mois, dates d'arrêtés préfectoraux de risque). |
| « Il y a dix ans » | Décennie récente (2016-2025) comparée à la précédente (2006-2015) | Couverture BDIFF de 20 ans pour la Gironde : affichée « depuis 2006 », à vérifier fichier ouvert. |
| « Végétation inflammable » | Surface de forêt (pins maritimes surtout) et de landes dans la commune | Typologie (essences de la BD Forêt, combustibilité) ; millésime de la cartographie pour la Gironde. |
| « Bâti au contact de la forêt » | Bâti à moins de 200 m d'une forêt (distance des obligations légales de débroussaillement) | Distance retenue ; disponibilité d'une couche bâti (BD TOPO). |
| « Population saisonnière » | Touristes en hébergement marchand et résidents secondaires | Aucune source ne la mesure directement : proxy (capacité d'hébergement touristique) à justifier. |
| « Renforts extra-départementaux » | Colonnes de renfort d'autres départements, moyens nationaux | Délai réel de mise en route (la veille suffit-il ?) ; décideur (zone de défense). |

## 5. Besoins

**Décision à éclairer** : savoir, la veille et en début de saison, où et quand engager les moyens du SDIS 33 (prépositionnement, saisonniers, renforts, protection de points sensibles) pour qu'un départ de feu ne devienne pas un grand feu comme Saumos 2026.

**Ce qui manque pour y répondre**

- Commanditaire et périmètre : hypothèse SDIS 33 (D01-D02).
- Seuil de « grand feu » : hypothèse 100 ha, paramétrable.
- Maille de prépositionnement réellement utilisée par le CODIS : inconnue.
- Données internes du SDIS (interventions, moyens engagés, effectifs) : probablement non publiques ; sans elles, on mesure le danger et les feux, pas l'effet des moyens.
- Horizon de prévision : J+1 seulement, ou aussi J+2 / J+3 pour les renforts.
- Niveau de détail acceptable sur les causes (risque de ré-identification d'un auteur).

## 6. Données idéales

| Question | Donnée idéale | Grain | Période | Fraîcheur | Emprise |
|---|---|---|---|---|---|
| Q1 | Danger météo de feu prévu à J+1 et observé, nombre historique de départs | zone (commune ou maille météo) × jour | ≈ 15 ans + prévision J+1 | quotidienne | Gironde |
| Q2 | Départs de feu datés (date d'alerte) | un feu | ≈ 20 ans (2006 → dernière année complète, à vérifier) | annuelle (bilan de saison) | Gironde (Landes en comparaison) |
| Q3 | Feux avec surface finale, danger du jour du départ, nombre de feux le même jour | un feu, avec le contexte de son jour | ≈ 20 ans | annuelle | Gironde + Landes (massif des Landes de Gascogne) |
| Q4 | Végétation (surface et essences), bâti, population résidente et saisonnière | commune × millésime | millésimes successifs disponibles | annuelle (population) ou pluriannuelle (végétation) | Gironde, communes en géographie de leur millésime |
