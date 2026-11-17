# Règles de qualité : seuil, action, test

Action : **bloquer** = test dbt `severity: error` ; **alerter** = `severity: warn` ; **tolérer** = règle documentée sans test bloquant. Chaque règle devient un test dbt (`dbt/tests/qrNN_*.sql` ou test générique déclaré dans les YAML) à l'étape où sa table existe.

| ID | Source | Règle | Seuil | Action | Défaillance | Étape du test |
|---|---|---|---|---|---|---|
| QR01 | BDIFF | `(annee, numero)` unique | 0 doublon | bloquer | — | T6 |
| QR02 | BDIFF | date d'alerte non nulle, année = année de la date | 0 écart | bloquer | — | T6 |
| QR03 | BDIFF | code commune au format `^(33\|40)[0-9]{3}$` | 0 écart | bloquer | — | T6 |
| QR04 | BDIFF | surface parcourue > 0 et < 100 000 ha | 0 écart | bloquer | — | T6 |
| QR05 | BDIFF | surface forêt ≤ surface parcourue | 0 écart | alerter | DQ04 | T6 |
| QR06 | BDIFF | somme des composantes ≤ surface parcourue (+1 m²) | ≤ 10 cas (4 connus) | alerter | DQ04 | T6 |
| QR07 | BDIFF | pas deux fiches même commune + même minute | 0 (37 connus) | alerter | DQ05 | T6 |
| QR08 | BDIFF | feux d'une année ≥ 50 % de la médiane des 10 années précédentes | par année | alerter | DQ02 | T6 |
| QR09 | BDIFF | code commune valide **à la date du feu** (COG historique) | rejets ≤ 1 % (warn si > 0) | alerter / bloquer au-delà de 1 % | DQ03 | T7 |
| QR10 | BDIFF | dernière campagne disponible = année N−1 | — | alerter | DQ01 | T6 |
| QR20 | Météo des forêts | niveaux J+1 et J+2 dans {1,2,3,4} | 0 écart | bloquer | — | T6 |
| QR21 | Météo des forêts | `(departement, date_emission)` unique | 0 doublon | bloquer | — | T6 |
| QR22 | Météo des forêts | code département normalisé présent dans le COG | 0 écart | bloquer | DQ07 | T6 |
| QR23 | Météo des forêts | aucun jour manquant entre le premier et le dernier bulletin de chaque saison, pour la Gironde | 0 jour | alerter | DQ07 | T6 |
| QR30 | FWI | FWI ≥ 0 et < 200 | 0 écart | bloquer | — | T6 |
| QR31 | FWI | `(date, latitude, longitude)` unique | 0 doublon | bloquer | — | T6 |
| QR32 | FWI | grille complète : 99 mailles chaque jour chargé | 0 jour incomplet | alerter | — | T6 |
| QR33 | FWI | dernière date ≥ aujourd'hui − 30 jours | — | alerter | DQ08 | T6 |
| QR34 | FWI | chaque commune de Gironde et des Landes a une maille | 0 commune sans maille | bloquer | DQ09 | T7 |
| QR40 | COG | périodes d'un même code sans chevauchement | 0 | bloquer | — | T6-T9 |
| QR41 | COG | `date_fin` > `date_debut` | 0 | bloquer | — | T6 |
| QR42 | COG | au plus une période ouverte par code | 0 | bloquer | — | T6 |
| QR50 | Hébergement | toutes les communes 33 et 40 du COG 2026 présentes | 100 % | bloquer | — | T7 |
| QR51 | Hébergement | valeurs ≥ 0 | 0 écart | bloquer | — | T6 |
| QR52 | Hébergement | total = somme des détails (campings) | 0 écart | alerter | DQ13 | T6 |
| QR60 | Population | toutes les communes 33 et 40 du COG 2026 présentes | 100 % | bloquer | — | T7 |
| QR61 | Population | somme des communes = total départemental | écart 0 | bloquer | — | T7 |
| QR62 | Population | PTOT ≥ PMUN | 0 écart | bloquer | — | T6 |
| QR70 | BD TOPO | `cleabs` unique | 0 | bloquer | — | T6 |
| QR71 | BD TOPO | bâtiments hors Gironde exclus, rejetés avec motif | rejets « sans aucune commune » ≤ 0,1 % | alerter | DQ10 | T7 |
| QR72 | ADMIN EXPRESS | communes = COG 2026 (33 et 40) | 0 écart | bloquer | — | T7 |

## Règles tolérées

| ID | Règle tolérée | Justification |
|---|---|---|
| QT1 | Cause du feu (`Nature`) vide pour 57 % des feux | Aucune des quatre décisions n'utilise la cause ; le champ n'est pas chargé (minimisation). |
| QT2 | `Précision des surfaces` vide avant 2023 | Changement de formulaire ; la précision n'entre dans aucun calcul. |
| QT3 | Végétation BD TOPO sans date de modification (76 %) | Pas d'alternative plus récente ouverte ; la limite est écrite sur la mesure (M6). |
| QT4 | `nombre_de_logements` vide pour 52 % des bâtiments | L'interface forêt-habitat compte des bâtiments, pas des logements, pour l'interface forêt-habitat. |
| QT5 | Saison seulement pour la Météo des forêts | Propriété du dispositif, pas une erreur : l'absence est codée `inconnu`. |
| QT6 | FWI sur des mailles marines | Exclues par construction (rattachement par centroïde de commune). |
