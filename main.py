#### Fonction secondaire
"""
code pour vérifier si des mots ou phrases sont des palindromes.
"""
def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome.
    
    Ignore la casse, les accents, et les caractères non-alphanumériques.

    Args:
        p (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si c'est un palindrome, False sinon.
    """
    # Dictionnaire pour les remplacements
    mydict = {"é": "e", "è": "e", "ê": "e", "à": "a", "â": "a",
              "ù": "u", "û": "u", "î": "i", "ô": "o", "ë": "e", "ç": "c"}
    mot = p.lower()
    for accent, sans_accent in mydict.items():
        mot = mot.replace(accent, sans_accent)
    mot_filtre = ""
    for caractere in mot:
        if caractere.isalnum():
            mot_filtre = mot_filtre + caractere
    mot_inverse = ""
    for caractere in mot_filtre:
        mot_inverse = caractere + mot_inverse
    return mot_filtre == mot_inverse

#### Fonction principale


def main():
    """
    Fonction principale pour tester la fonction ispalindrome.

    Args:
        Aucun.

    Returns:
        Rien.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
