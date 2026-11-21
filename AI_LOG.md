# AI_LOG.md

## Utilisation de l'assistance IA

Le projet a été réalisé en binôme. Les membres ont participé à la réflexion, aux décisions techniques et à l'avancement du projet. L'assistance IA a été utilisée comme outil complémentaire. Les propositions générées ont été examinées et adaptées par les membres du binôme.

### Tâche 1 – Compréhension des consignes et des notions

- **Outil :** ChatGPT
- **Utilisation :** Demande d'explications sur les consignes du projet, les User Stories, les critères d'acceptation et le fonctionnement du Planning Poker.
- **Apport de l'IA :** Clarification des notions et aide à la compréhension du travail demandé.
- **Travail du binôme :** Analyse des consignes, échanges et choix des fonctionnalités à réaliser.

### Tâche 2 – Rédaction et mise en forme du R1

- **Outil :** ChatGPT
- **Utilisation :** Aide à la correction, à la structuration et à la mise en forme Markdown du document R1.
- **Apport de l'IA :** Suggestions de reformulation et aide à la vérification de la cohérence entre R0 et R1.
- **Travail du binôme :** Réalisation des estimations, votes, débats et validation des décisions retenues dans le document.

### Tâche 3 – Aide à Git et à l'organisation du projet

- **Outil :** ChatGPT
- **Utilisation :** Demande d'explications sur les commandes Git, les branches, les commits, les push et les Pull Requests.
- **Apport de l'IA :** Explication des commandes et accompagnement dans les étapes de gestion du dépôt GitHub.
- **Travail du binôme :** Exécution des commandes, gestion des branches et validation des modifications.

### Tâche 4 – Aide à la compréhension et à l'implémentation du moteur de règles (R2)

- **Outil :** ChatGPT
- **Utilisation :** Demande d'explications sur les règles de validation, les cas d'acceptation, la médiane et la gestion des situations particulières.
- **Apport de l'IA :** Aide à la formalisation des règles métier et à la compréhension de la logique de la fonction `verifier_tour`.
- **Travail du binôme :** Choix des comportements attendus, adaptation du moteur de règles et organisation des fichiers Python.

### Tâche 5 – Mise en place de l'intégration continue

- **Outil :** ChatGPT
- **Utilisation :** Demande d'explications sur GitHub Actions et aide à la préparation du fichier de configuration `ci.yml`.
- **Apport de l'IA :** Accompagnement dans la configuration du workflow et l'interprétation des résultats d'exécution.
- **Travail du binôme :** Ajout du workflow dans `.github/workflows/ci.yml`, publication sur GitHub et vérification du résultat.
- **Résultat vérifié :** Le workflow « Tests Python » s'est exécuté avec succès sur GitHub Actions.

### Tâche 6 – Aide à la rédaction du R2

- **Outil :** ChatGPT
- **Utilisation :** Aide à la structuration du compte rendu, à la rédaction des explications sur le TDD et à la présentation des résultats.
- **Apport de l'IA :** Suggestions de formulation et aide à la vérification de la cohérence entre les tests, le moteur de règles et la documentation.
- **Travail du binôme :** Vérification des informations, validation des décisions métier et préparation du rendu final.

## Entrée 3 : Squelette Python du walking skeleton (US-01, US-02)

- **Demande :** Aide à la compréhension et à la mise en place du code de saisie du nombre de joueurs et des pseudos, ainsi que du chargement d'un backlog JSON, avec séparation `core` / `persistence` / `ui`.
- **Résultat :** Le code a été adapté, notamment au niveau de l'appel du fichier `backlog.json` dans `main.py`.
- **Vérifié :** À compléter avec les tests réellement effectués par le binôme.
- **Changé ou rejeté :** Adaptation des chemins de fichiers et des imports à l'arborescence réelle du projet.

## Limites de l'assistance IA

L'assistance IA n'a pas remplacé le travail du binôme. Les décisions métier, les choix de conception, les vérifications du code et la validation des livrables restent sous la responsabilité des membres du projet.

GitHub Actions a été utilisé pour l'intégration continue. GitHub Copilot n'a pas été utilisé pour les travaux décrits dans ce journal.