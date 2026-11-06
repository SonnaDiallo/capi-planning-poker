from dataclasses import dataclass

MIN_JOUEURS = 2
MAX_JOUEURS = 10


class ErreurConfiguration(ValueError):
    """Configuration de partie invalide."""


@dataclass
class Fonctionnalite:
    id: str
    titre: str


def valider_nombre_joueurs(nombre):
    if not MIN_JOUEURS <= nombre <= MAX_JOUEURS:
        raise ErreurConfiguration(
            f"Le nombre de joueurs doit être entre {MIN_JOUEURS} et {MAX_JOUEURS}."
        )
    return nombre


def valider_pseudos(pseudos):
    propres = [p.strip() for p in pseudos]
    if any(p == "" for p in propres):
        raise ErreurConfiguration("Un pseudo ne peut pas être vide.")
    if len({p.lower() for p in propres}) != len(propres):
        raise ErreurConfiguration("Les pseudos doivent être uniques.")
    return propres