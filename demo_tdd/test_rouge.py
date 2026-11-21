from regles import verifier_tour


def test_mediane_deuxieme_tour():
    resultat = verifier_tour([2, 5, 13], 2, "mediane")

    assert resultat["valide"] is True
    assert resultat["valeur"] == 5