import os

from src.core.cards import CARTES, convertir_carte
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


def saisir_regle():
    while True:
        choix = input("Règle de validation (stricte / mediane) : ").strip().lower()
        if choix in ("stricte", "mediane"):
            return choix
        print("Règle inconnue.")


def effacer_ecran():
    os.system("cls" if os.name == "nt" else "clear")


def demander_vote(pseudo):
    while True:
        saisie = input(f"{pseudo}, votre carte {CARTES} : ")
        carte = convertir_carte(saisie)
        if carte is not None:
            effacer_ecran()
            return carte
        print("Carte invalide.")


def afficher_votes(pseudos, votes):
    print("\nRévélation des votes :")
    for pseudo, vote in zip(pseudos, votes):
        print(f"  {pseudo} : {vote}")