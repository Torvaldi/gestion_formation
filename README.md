# Module Odoo - Gestion des formations

## Auteur

Quentin LAURENT - LPRO CASIR

## Compte-rendu

### Dossier `controllers`

Ce dossier permet de gérer toute la partie back-office du module. Il gère la récupération des données et les routes. Dans ce cas précis, il a été auto-généré par la commande `odoo-bin scaffold gestion_formation ./`.

### Dossier `models`

Le dossier contient tous ce qui concerne les différentes tables en base de données pour le module. On peut aussi y ajouter la validation des données mais aussi les différentes relations entre les tables.

### Dossier `security`

Le dossier contient la gestion de la sécurité du module avec la possibilité de laisser ou de bloquer les accès en fonction des droits et des groupes.

### Dossier `views`

Ce dossier contient les différentes vues du système avec les templates (modèle de vue), les différentes vues (kanban, form...) mais aussi le module de gestion création de rôles.

### Fichier `__manifest__.py`

Défini les différentes propriétés du module comme son nom, les dépendances, une description ou encore l'auteur etc...

### Fichier `__init__.py`

Initialise les controllers et les models du module.

## Ce qui n'a pas été implémenté

### Partie 1

- Les parties concernant le Kanban, où il m'a été impossible de trouver un tutoriel/module compréhensible ou fonctionnel

### Partie 2

- Question 2 (et donc 3 et 4) car je n'ai pas compris comment générer le bouton et les actions correspondantes.