def verifier_tour(votes, tour, regle):
    if not votes:
        return {"valide": False, "action": "revote"}

    if sum(1 for v in votes if v == "cafe") == 1:
        return {"valide": False, "action": "reprendre"}

    premier = votes[0]
    identiques = all(v == premier for v in votes)

    if tour == 1 or (tour == 2 and regle == "stricte"):
        return {
            "valide": identiques,
            "valeur": premier if identiques else None,
            "action": "valide" if identiques else "revote",
        }

    return {"valide": False, "action": "revote"}
