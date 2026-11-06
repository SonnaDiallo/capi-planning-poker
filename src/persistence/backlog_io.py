import json

from src.core.models import Fonctionnalite


class ErreurBacklog(Exception):
    """Backlog absent, illisible ou invalide."""


def charger_backlog(chemin):
    try:
        with open(chemin, encoding="utf-8") as f:
            donnees = json.load(f)
    except FileNotFoundError:
        raise ErreurBacklog(f"Fichier introuvable : {chemin}")
    except json.JSONDecodeError:
        raise ErreurBacklog("Le fichier n'est pas un JSON valide.")

    try:
        projet = donnees["projet"]
        brutes = donnees["fonctionnalites"]
        fonctionnalites = [Fonctionnalite(f["id"], f["titre"]) for f in brutes]
    except (KeyError, TypeError):
        raise ErreurBacklog(
            "Structure invalide : attendu 'projet' et une liste 'fonctionnalites' "
            "avec 'id' et 'titre'."
        )

    if not fonctionnalites:
        raise ErreurBacklog("Le backlog est vide.")
    return projet, fonctionnalites