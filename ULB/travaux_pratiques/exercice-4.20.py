def chiffrer(texte: str, decalage: int) -> str:
    texte_chiffre = ""
    for i in range(len(texte)):
        if ord("A") <= i <= ord("Z"):
            texte_chiffre += chr((ord(texte[i]) + decalage) % ord("Z"))
        else:
            texte_chiffre += chr((ord(texte[i]) + decalage) % ord("z"))

    return texte_chiffre


print(chiffrer("BONJOUR", 3))
