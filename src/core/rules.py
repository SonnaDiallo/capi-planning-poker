def verifier_tour(votes, tour, regle):
    resultat = {
        "valide": False,
        "valeur": None,
        "action": "revote"
    }

    # Aucun vote
    if not votes:
        return resultat

    # Tous les joueurs choisissent Café
    if all(v == "cafe" for v in votes):
        resultat["action"] = "pause"
        return resultat

    # Un vote Café parmi les autres votes
    if "cafe" in votes:
        resultat["action"] = "reprendre"
        return resultat

    # Au moins un joueur exprime une incertitude
    if "?" in votes:
        resultat["action"] = "discussion"
        return resultat

    # Premier tour : unanimité obligatoire
    if tour == 1:
        pareil = all(v == votes[0] for v in votes)

        if pareil:
            return {
                "valide": True,
                "valeur": votes[0],
                "action": "valide"
            }

        return resultat

    # Tours suivants : règle stricte
    if regle == "stricte":
        pareil = all(v == votes[0] for v in votes)

        if pareil:
            return {
                "valide": True,
                "valeur": votes[0],
                "action": "valide"
            }

        return resultat

    # Tours suivants : règle médiane
    if regle == "mediane":
        if not all(isinstance(v, (int, float)) for v in votes):
            return resultat

        votes_tries = sorted(votes)
        indice = (len(votes_tries) - 1) // 2
        mediane = votes_tries[indice]

        return {
            "valide": True,
            "valeur": mediane,
            "action": "valide"
        }

    return resultat