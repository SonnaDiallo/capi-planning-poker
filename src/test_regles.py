
from src.regles import verifier_tour


def test_tout_le_monde_pareil():
    resultat = verifier_tour([5, 5, 5], 1, "stricte")
    assert resultat["valide"] is True
    assert resultat["valeur"] == 5


def test_votes_differents():
    resultat = verifier_tour([3, 5, 8], 1, "stricte")
    assert resultat["valide"] is False


def test_deuxieme_tour_strict():
    resultat = verifier_tour([5, 5, 8], 2, "stricte")
    assert resultat["valide"] is False
