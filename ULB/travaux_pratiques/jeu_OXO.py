def initialiser_plateau() -> list:
    return [[None for j in range(3)] for i in range(3)]


def afficher_plateau(plateau: list[list]):
    for i in range(len(plateau)):
        end = " | "
        for j in range(len(plateau[i])):
            if j == len(plateau[i]) - 1:
                end = ""
            if [i][j] is None:
                print(" ", end=end)
            else:
                print(plateau[i][j], end=end)

        print()


def jouer(plateau: list[list], joueur: str, ligne: int, colonne: int):
    if not (0 <= ligne < 3) or not (0 <= colonne < 3):
        print("Indice(s) incorrect(s).")
    else:
        plateau[ligne][colonne] = joueur


p = initialiser_plateau()
afficher_plateau(p)
jouer(p, "X", 1, 1)


def verifier_diagonale(plateau, joueur):

    diagonale_gagnante = True
    for i in range(len(plateau)):
        if plateau[i][i] != joueur:
            diagonale_gagnante = False
        if plateau[i][len(plateau) - 1 - i] != jouer:
            diagonale_gagnante = False
    return diagonale_gagnante


def verifier_colonne(plateau, joueur):
    for colonne in range(len(plateau[0])):
        colonne_gagnante = True
        for ligne in range(len(plateau)):
            if plateau[ligne][colonne] != joueur:
                colonne_gagnante = False
        if colonne_gagnante:
            return True
    return False


def verifier_ligne(plateau, joueur):
    for i in range(len(plateau[0])):
        if plateau[i] == [joueur] * len(plateau[i]):
            return True
    return False


def a_gagner(plateau, joueur) -> bool:
    return (
        verifier_colonne(plateau, joueur)
        or verifier_ligne(plateau, joueur)
        or verifier_colonne(plateau, joueur)
    )
