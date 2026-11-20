def verifier_tour(votes, tour, regle):
    nb = sum(1 for v in votes if v == "cafe")

    # Si un seul joueur choisit cafe, on reprend
    if nb == 1:
        return {"valide": False, "action": "reprendre"}

    if not votes:
        return {"valide": False, "action": "revote"}

    vote = votes[0]
    pareil = all(v == vote for v in votes)

    # Tour 1 : tout le monde doit etre d'accord
    if tour == 1:
        return {
            "valide": pareil,
            "valeur": vote if pareil else None,
            "action": "valide" if pareil else "revote",
        }

    # Tour 2 : regle stricte
    if tour == 2 and regle == "stricte":
        return {
            "valide": pareil,
            "valeur": vote if pareil else None,
            "action": "valide" if pareil else "revote",
        }

    return {"valide": False, "action": "revote"}
