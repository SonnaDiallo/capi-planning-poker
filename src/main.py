import sys

from src.persistence.backlog_io import ErreurBacklog, charger_backlog
from src.ui import console


def main():
    chemin = sys.argv[1] if len(sys.argv) > 1 else "exemples/backlog.json"

    nombre = console.saisir_nombre_joueurs()
    pseudos = console.saisir_pseudos(nombre)
    print(f"Joueurs : {', '.join(pseudos)}")

    try:
        projet, fonctionnalites = charger_backlog(chemin)
    except ErreurBacklog as e:
        print(f"Erreur : {e}")
        return

    print(f"Projet : {projet} ({len(fonctionnalites)} fonctionnalités)")
    console.afficher_fonctionnalite(fonctionnalites[0])


if __name__ == "__main__":
    main()