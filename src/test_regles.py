from src.regles import verifier_tour


def test_unanimite_premier_tour():
    resultat = verifier_tour([5, 5, 5], 1, "stricte")
    assert resultat["valide"] is True
    assert resultat["valeur"] == 5


def test_desaccord_premier_tour():
    resultat = verifier_tour([3, 5, 8], 1, "stricte")
    assert resultat["valide"] is False


def test_regle_stricte_deuxieme_tour():
    resultat = verifier_tour([5, 5, 8], 2, "stricte")
    assert resultat["valide"] is False
