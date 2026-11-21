
from src.core.rules import verifier_tour


def test_CA_04_1_regle_stricte():
    resultat = verifier_tour([2, 3, 5, 8], 1, "stricte")
    assert resultat["valide"] is False
    assert resultat["action"] == "revote"


#CA-04.2 : l'unanimité prime sur la médiane au premier tour.
def test_CA_04_2_unanimite_premier_tour():
    resultat = verifier_tour([3, 3, 3, 5], 1, "mediane")
    assert resultat["valide"] is False
    assert resultat["action"] == "revote"


#test mediane avec nombre impair de votes
def test_CA_04_3_mediane_nb_impair():
    resultat = verifier_tour([2, 5, 13], 2, "mediane")
    assert resultat["valide"] is True
    assert resultat["valeur"] == 5


#CA-04.4 : la convention de médiane inférieure pour un nombre pair.
def test_CA_04_4_mediane_nb_pair():
    resultat = verifier_tour([5, 8, 3, 13], 2, "mediane")
    assert resultat["valide"] is True
    assert resultat["valeur"] == 5


#-CA-04.5 : le vote ? empêche la validation malgré les autres votes identiques.
def test_CA_04_5_vote_avec_incertitude():
    resultat = verifier_tour([5, 5, 5, "?"], 2, "stricte")
    assert resultat["valide"] is False
    assert resultat["valeur"] is None
    assert resultat["action"] == "discussion"

#Validation par unanimité stricte

def test_CA_04_6_unanimite_regle_stricte():
    resultat = verifier_tour([5, 5, 5], 1, "stricte")
    assert resultat["valide"] is True
    assert resultat["valeur"] == 5


#pause café
def test_CA_06_1_pause_cafe():
    resultat = verifier_tour(["cafe", "cafe", "cafe"], 1, "stricte")
    assert resultat["valide"] is False
    assert resultat["valeur"] is None
    assert resultat["action"] == "pause"
