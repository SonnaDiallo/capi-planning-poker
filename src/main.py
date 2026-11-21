import sys

from src.core.game import estimer_fonctionnalite
from src.persistence.backlog_io import ErreurBacklog, charger_backlog
from src.ui import console


def main():
    chemin = sys.argv[1] if len(sys.argv) > 1 else "exemples/backlog.json"

    nombre = console.saisir_nombre_joueurs()
    pseudos = console.saisir_pseudos(nombre)
    regle = console.saisir_regle()

    try:
        projet, fonctionnalites = charger_backlog(chemin)
    except ErreurBacklog as e:
        print(f"Erreur : {e}")
        return

    print(f"Projet : {projet} ({len(fonctionnalites)} fonctionnalités)")

    estimations = {}
    for fonctionnalite in fonctionnalites:
        console.afficher_fonctionnalite(fonctionnalite)
        statut, valeur = estimer_fonctionnalite(
            pseudos, regle, console.demander_vote, console.afficher_votes
        )
        if statut == "pause":
            print("Pause café : la partie s'arrête (sauvegarde pas encore implémentée).")
            return
        estimations[fonctionnalite.id] = valeur
        print(f"Estimation validée : {valeur}")

    print("\nBacklog estimé :")
    for identifiant, valeur in estimations.items():
        print(f"  {identifiant} : {valeur}")


if __name__ == "__main__":
    main()