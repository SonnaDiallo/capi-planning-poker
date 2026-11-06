from src.core.models import (
    ErreurConfiguration,
    valider_nombre_joueurs,
    valider_pseudos,
)


def saisir_nombre_joueurs():
    while True:
        try:
            return valider_nombre_joueurs(int(input("Nombre de joueurs : ")))
        except ValueError as e:
            print(f"Entrée invalide : {e}")


def saisir_pseudos(nombre):
    while True:
        pseudos = [input(f"Pseudo du joueur {i + 1} : ") for i in range(nombre)]
        try:
            return valider_pseudos(pseudos)
        except ErreurConfiguration as e:
            print(f"{e} Recommencez la saisie.")


def afficher_fonctionnalite(fonctionnalite):
    print(f"\nFonctionnalité à estimer : [{fonctionnalite.id}] {fonctionnalite.titre}")