from src.core.rules import verifier_tour


def estimer_fonctionnalite(pseudos, regle, demander_vote, afficher_votes):
    """Fait voter les joueurs jusqu'à validation ou pause.

    Renvoie ("valide", valeur) ou ("pause", None).
    """
    tour = 1
    while True:
        votes = [demander_vote(pseudo) for pseudo in pseudos]
        afficher_votes(pseudos, votes)
        resultat = verifier_tour(votes, tour, regle)

        if resultat["action"] == "valide":
            return "valide", resultat["valeur"]
        if resultat["action"] == "pause":
            return "pause", None
        if resultat["action"] != "reprendre":
            tour += 1