# AI_LOG.md

## Utilisation de l'assistance IA

Le projet a été réalisé en binôme. Les membres ont participé à la réflexion, aux décisions et à l'avancement du projet. L'assistance IA a été utilisée comme outil complémentaire.

### Tâche 1 – Compréhension des consignes et des notions
- **Outil :** ChatGPT
- **Utilisation :** Demande d'explications sur les consignes du projet, les User Stories, les critères d'acceptation et le Planning Poker.
- **Apport de l'IA :** Clarification des notions et aide à la compréhension du travail demandé.
- **Travail du binôme :** Échanges, analyse des consignes et choix des fonctionnalités à réaliser.

### Tâche 2 – Rédaction et mise en forme du R1
- **Outil :** ChatGPT
- **Utilisation :** Aide à la correction, à la structuration et à la mise en forme Markdown du document R1.
- **Apport de l'IA :** Suggestions de reformulation, vérification de la cohérence entre R0 et R1 et amélioration des critères d'acceptation.
- **Travail du binôme :** Réalisation des estimations, votes, débats et validation des décisions retenues dans le document.

### Tâche 3 – Aide à Git et à l'organisation du projet
- **Outil :** ChatGPT
- **Utilisation :** Demande d'explications sur les commandes Git, les branches et les Pull Requests.
- **Apport de l'IA :** Accompagnement et explication des différentes étapes de gestion du dépôt.
- **Travail du binôme :** Travail collaboratif sur le projet, utilisation des outils et gestion du code.

## Entrée 3 : squelette Python du walking skeleton (US-01, US-02)
- **Demande :** code de saisie du nombre de joueurs et des pseudos, et de chargement d'un backlog JSON, avec séparation `core` / `persistence` / `ui`.
- **Résultat :** [modifié au niveau de l'appel du fichier backlog.json au niveau de main.py ].
- **Vérifié :** [lancement avec `python -m src.main`, 1 et 11 joueurs, pseudo vide, doublon, fichier inconnu, JSON cassé].
- **Changé ou rejeté :** [ex. : espace corrigé dans le JSON, imports adaptés à notre arborescence].