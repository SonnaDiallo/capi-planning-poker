CARTES = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100, "?", "cafe"]


def convertir_carte(saisie):
    """Renvoie la carte correspondant à la saisie, ou None si elle est invalide."""
    texte = saisie.strip().lower()
    if texte in ("?", "cafe", "café"):
        return "cafe" if texte.startswith("caf") else "?"
    try:
        valeur = int(texte)
    except ValueError:
        return None
    return valeur if valeur in CARTES else None