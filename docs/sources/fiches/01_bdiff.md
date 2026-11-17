# Fiche 01 — BDIFF (Base de données des incendies de forêt en France)

Fichier ouvert le 17/11/2026.

| Rubrique | Valeur |
|---|---|
| Propriétaire | Ministère de l'Agriculture (MASA, DGPE) ; site conçu par l'IGN ; saisie par les services départementaux (SDIS, DDT) : détail par département `non vérifié`. |
| Accès (URL) | Catalogue : https://www.data.gouv.fr/datasets/base-de-donnees-sur-les-incendies-de-forets-en-france-bdiff (lien vers le portail). Données : https://bdiff.agriculture.gouv.fr/incendies, recherche (`if[deprts][value]=33,40`, dates d'alerte) puis `GET /incendies/zip`. Public, sans compte. **Obstacle O03** : chaîne TLS mal configurée ; contournement par l'intermédiaire officiel HARICA, vérification TLS maintenue. |
| Contenu | Zip : `Incendies.csv` (UTF-8, `;`, 3 lignes de métadonnées avant l'en-tête), `Définitions.pdf`, `Mention légales.pdf`. 24 colonnes : année, numéro, département, code INSEE, commune, date et heure d'alerte, surfaces par végétation (m²), nature (cause), décès / bâtiments détruits… Filtre « Type de feu : F » (incendie de forêt). Zip non déterministe (horodatage) ; CSV déterministe. 5 460 lignes, 357 692 octets (Gironde seule). SHA-256 du CSV 33+40 : `00787e13052709c6…`. |
| Granularité | **Un feu** ; localisation à la commune de départ, sans coordonnées. |
| Historique | 20 campagnes (2006-2025) : 3 555 feux en Gironde, 1 905 dans les Landes, du 05/02/2006 au 28/12/2025. Le catalogue annonce 2006-2022 : fiche catalogue en retard. |
| Fraîcheur | Annuelle, « jusqu'à l'année antérieure à l'année en cours ». **Campagne 2026 (Saumos) absente.** |
| Clés | `(Année, Numéro)` unique (5 460 couples pour 5 460 lignes ; `Numéro` seul non unique) ; `Code INSEE`. |
| Licence | **Contradiction (obstacle O04)** : « Licence Ouverte v2.0 » sur data.gouv.fr, mais les mentions légales jointes (§7) interdisent la vente et toute modification, imposent la citation et réservent les droits de reproduction. |
| Millésime | Extraction du 17/11/2026, campagnes 2006-2025. Définition des surfaces par végétation différente avant et après 2023. |
| Référentiel géographique | Code commune en vigueur à la date du feu : 33 feux (20 en Gironde, 13 dans les Landes) ont un code absent du COG 2026 (ex. 33267 Marcillac, fusion 2019), **0** code invalide à sa date selon `v_commune_depuis_1943`. 373 libellés pour 369 codes en Gironde : jointure sur le code. |
| Données personnelles | Aucun nom. **Indirectement personnelles** : commune + date + heure + nature « Malveillance » ou « Involontaire (particulier) » peuvent désigner une personne dans une petite commune (recoupement presse) ; de même pour décès et bâtiments détruits. |
| Questions servies | Q1 (historique des départs), Q2 (dates), Q3 (surface finale, feux du même jour). |
| Premiers constats qualité | Cause renseignée pour 38,5 % des feux de Gironde ; `Précision des surfaces` à 19 % ; `Type de peuplement` et `Surface maquis garrigues` vides (hors zone méditerranéenne) ; 1 seul feu à 00:00 ; aucune surface nulle. Landiras 2022 en deux fiches (12/07 : 12 552 ha ; 12/08 : 6 743 ha). 2024 : 29 feux seulement en Gironde (à surveiller). |
| Décision | **Retenue** : seule source des départs de feu datés (Q2) et de la surface finale (Q3). |
