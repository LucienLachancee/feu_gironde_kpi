# Modèle de risque localisé par température du sol

Projet feux de forêt · Gironde · G14 · note de conception, novembre 2026

## En une phrase

Utiliser la température du sol mesurée par satellite pour indiquer au SDIS 33, chaque jour de juin, les zones d'environ 1 km où un départ de feu risque le plus de devenir un grand feu, afin d'y envoyer un renfort ciblé.

## Le problème

| Constat | Source |
|---|---|
| En juin, un jour compte environ un tiers des départs d'un jour de juillet-août (K1 médian : 34,4 %) | Atelier 1, partie E |
| Un renfort complet dès le 1er juin paraît donc disproportionné, mais ne rien faire laisse ce tiers d'activité sans renfort | Question Q2 |
| Un renfort partiel n'est utile que s'il est placé au bon endroit | — |
| L'indice de danger météo (FWI) disponible découpe la Gironde en cases d'environ 25 km : trop grossier pour choisir où envoyer une équipe | Fiche source CEMS |

## Ce que fait la fonctionnalité

1. Chaque nuit, elle récupère la température du sol des 7 derniers jours.
2. Elle calcule, pour chaque zone d'environ 1 km, la probabilité qu'un feu qui y partirait dépasse 1 ha.
3. Le matin, elle fournit aux équipes une carte des zones prioritaires, consultable sur tablette, même sans réseau.

## Hypothèses

| # | Hypothèse | Comment la tester | Statut |
|---|---|---|---|
| H1 | Un sol plus chaud sur 7 jours signale une végétation plus sèche, où les feux grandissent plus vite | Comparer la température du sol avant les feux de plus de 1 ha et avant les autres | À tester |
| H2 | À danger FWI égal, dans une même case de 25 km, les grands feux partent dans les zones les plus chaudes | Comparaison à l'intérieur de chaque case, à FWI égal | À tester : c'est le cœur de l'idée |
| H3 | Le modèle « FWI + température du sol » prévoit au moins aussi bien que le « FWI seul » | Comparaison sur des années non vues par le modèle | À tester |
| H4 | Un renfort ciblé couvre l'essentiel de l'activité de juin à moindre coût | Nécessite les effectifs et les interventions du SDIS | Non testable avec des données publiques |

## Pourquoi le faire

- **Une précision de lieu que le FWI n'a pas** : environ 1 km au lieu de 25 km. Même si la température du sol ne prévoyait pas mieux le moment des feux, elle dirait mieux où.
- **Une mesure observée**, et non calculée à partir de stations météo.
- **Une option intermédiaire crédible pour Q2** : un petit renfort mobile, placé chaque jour selon la carte, entre le statu quo et le renfort complet au 1er juin.
- **Une réponse à la question « pourquoi les feux de juin restent-ils plus souvent petits ? »** : en proportion, ils dépassent moins souvent 1 ha qu'en juillet-août (K4 : −15 points). Si l'effet du mois disparaît une fois la température du sol et le FWI pris en compte, la météo suffit à l'expliquer.

## Ce qu'elle ne fait pas

- **Elle ne prévoit pas les départs de feu.** Un départ demande une étincelle, souvent d'origine humaine. La carte indique où un feu grandirait vite, pas où il partira.
- **Elle n'agit pas à la source.** Pour le SDIS, « agir » veut dire surveiller et prépositionner. Le débroussaillement et les interdictions d'accès relèvent des maires et du préfet.
- **Elle ne voit pas sous les nuages.** Le satellite passe une ou deux fois par jour ; les jours couverts, la moyenne sur 7 jours comble les trous.

## Données

| Donnée | Producteur | Maille | Période | Accès | Statut |
|---|---|---|---|---|---|
| Départs de feu (BDIFF) | Ministère de l'Agriculture | Commune | 2006‑2025 | Public | Utilisée dans l'atelier |
| Danger météo (FWI, CEMS) | Copernicus | Environ 25 km | 2006‑2026 | Compte gratuit | Dans l'entrepôt |
| Température du sol (MODIS, produit MOD11A1) | NASA | Environ 1 km | Depuis 2000 | Compte NASA Earthdata gratuit | À vérifier |
| Contours des communes (ADMIN EXPRESS) | IGN | Commune | 2026 | Public | Dans l'entrepôt |

## Le modèle

| Élément | Choix |
|---|---|
| Entrées | Température du sol sur 7 jours, FWI du jour, mois, type de végétation (option) |
| Sortie | Probabilité qu'un feu dépasse 1 ha |
| Méthode | Régression logistique : quelques coefficients, explicable formule par formule |
| Apprentissage | Feux de 2006 à 2020, Gironde (Landes ajoutées si trop peu de grands feux) |
| Évaluation | Test sur 2021-2025, années jamais vues, comparé au modèle « FWI seul » |

**Pourquoi un modèle simple.** Il y a peu de grands feux en juin : un modèle complexe apprendrait du bruit. Une formule à quelques coefficients s'explique à un décideur et se calcule sur n'importe quel téléphone.

## Utilisation sur le terrain

| Quand | Où | Quoi |
|---|---|---|
| Chaque nuit | Au centre de traitement | Téléchargement des images, nettoyage des nuages, calcul de la carte de risque |
| Le matin | Sur les tablettes | Réception d'une carte légère ou d'une liste de zones prioritaires, consultable sans réseau |

Le calcul lourd ne se fait jamais sur la tablette : en forêt, le réseau mobile est souvent absent. C'est le critère Easy de RACER.

## Étapes de réalisation

| # | Étape | Résultat attendu |
|---|---|---|
| 1 | Accéder aux données de température du sol et mesurer les jours manquants à cause des nuages | Une couverture suffisante en juin, ou l'abandon documenté |
| 2 | Construire une ligne par feu : température sur 7 jours, FWI, mois, taille finale | Le jeu de données du modèle |
| 3 | Comparer « à danger égal » la part des feux de plus de 1 ha, en juin et en juillet-août | Un premier test de H1 et H2, sans modèle |
| 4 | Entraîner et comparer les deux modèles | Le test de H3 |
| 5 | Produire la carte de risque d'un jour de juin passé | Un prototype à montrer |

**Règle de décision.** Si H2 et H3 sont confirmées, on passe au prototype. Sinon, on le documente et le SDIS garde le FWI.

## Questions ouvertes

- Quels effectifs le SDIS a-t-il déjà en juin ? Sans cette donnée, H4 reste une hypothèse.
- Les seuils des classes de danger FWI sont encore marqués « non vérifiés ».
- Le seuil de 1 ha pour définir un feu qui « grandit » est à faire valider.
- L'accès aux données de température du sol demande un compte, à créer par l'équipe.

## Perspective

Calculé chaque jour de juillet-août, le même modèle indiquerait où placer les renforts déjà en place : une piste pour répondre à la question Q1 (« demain, quelles zones surveiller en priorité ? »).
