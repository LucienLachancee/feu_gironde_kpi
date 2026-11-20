# Matrice questions × sources

Légende : **C** couvre · **P** couvre en partie · **–** ne couvre pas · **?** inconnu (fichier non ouvert).
Q1 prépositionnement J+1 · Q2 calendrier des saisonniers · Q3 renforts (seuil de grand feu) · Q4 protection des points sensibles · Réf. = rattachement des autres sources (clé ou géométrie).

| # | Source | Q1 | Q2 | Q3 | Q4 | Réf. |
|---|---|---|---|---|---|---|
| 01 | BDIFF (33, 40) | P (historique des départs, pas de prévision) | **C** (date et heure de chaque départ, 2006-2025) | P (surface finale, feux du même jour ; pas le danger) | – | – |
| 02 | FWI CEMS (réanalyse) | P (danger par maille et par jour, observé et non prévu) | – | **C** (danger du jour du départ) | – | – |
| 03 | Météo des forêts | P (seule prévision J+1 ; par département, en saison, depuis 2024) | – | P (niveau prévu la veille, 2024-2026) | – | – |
| 04 | Climatologie quotidienne Météo-France | P (IFM à recalculer) | – | P | – | – |
| 05 | IFM horaire communautaire | ? (inaccessible) | – | ? | – | – |
| 06 | COG + historique INSEE | – | – | – | – | **C** (codes, périodes de validité) |
| 07 | ADMIN EXPRESS COG CARTO 2026 | – | – | – | P (contours pour rattacher bâti et végétation) | **C** (contours, centroïdes) |
| 08 | BD Forêt V2 (2009) | – | – | – | P (essences, mais 2009) | – |
| 09 | BD TOPO (bâti + végétation, 2026) | – | – | – | **C** (bâti, végétation inflammable) | – |
| 10 | Hébergement touristique INSEE | – | – | – | P (proxy saisonnier, hébergement marchand seulement) | – |
| 11 | Populations légales INSEE | – | – | – | **C** (population résidente) | – |
| 12 | EFFIS | ? | – | ? | – | – |
| 13 | Prométhée | – | – | – | – | – |
| 14 | Données internes SDIS 33 | ? (effet des moyens prépositionnés) | P (effectifs actuels) | ? (moyens engagés, renforts) | – | – |

## Décisions

**8 sources retenues** (cible : 5 à 8). Les manques sont traités dans [`manques.md`](manques.md).

| # | Source | Décision | Raison |
|---|---|---|---|
| 01 | BDIFF | Retenue | Seule source des départs datés et des surfaces finales (Q1, Q2, Q3). |
| 02 | FWI CEMS | Retenue | Danger par maille et par jour, y compris le jour de chaque départ (Q1, Q3). |
| 03 | Météo des forêts | Retenue | Seule prévision J+1 ouverte (Q1, Q3). |
| 06 | COG INSEE | Retenue | Sans question propre, indispensable aux jointures (feu de 2013 → commune de 2013). |
| 07 | ADMIN EXPRESS | Retenue | Sans question propre, indispensable aux jointures (maille météo → commune, bâtiment → commune). |
| 09 | BD TOPO | Retenue | Bâti et végétation inflammable récents (Q4). |
| 10 | Hébergement touristique | Retenue | Proxy de la population saisonnière (Q4). |
| 11 | Populations légales | Retenue | Population résidente (Q4). |
| 04 | Climatologie Météo-France | Écartée | Recalcul de l'IFM lourd ; vent manquant pour la moitié des 21 stations ; le FWI CEMS fournit le même indice (méthode canadienne) sur grille complète. À reconsidérer si le FWI CEMS cesse d'être mis à jour (O06). |
| 05 | IFM communautaire | Rejetée | Inaccessible, sans garantie de qualité selon son auteur. |
| 08 | BD Forêt V2 | Écartée | Millésime 2009 ; la BD TOPO 2026 (même producteur) distingue déjà conifères, feuillus, mixte et landes ligneuses ; deux mesures concurrentes de la même surface sinon. Perte faible : 222 194 ha de pin maritime pur sur 223 346 ha de forêt fermée de conifères. |
| 12 | EFFIS | Écartée | Non téléchargeable (O07) ; contexte seulement, aucune décision. Perte : emprise de Saumos 2026. |
| 13 | Prométhée | Écartée | Hors emprise (zone méditerranéenne). |
| 14 | Données internes SDIS 33 | Manque | Non publiques : décision M5. |
