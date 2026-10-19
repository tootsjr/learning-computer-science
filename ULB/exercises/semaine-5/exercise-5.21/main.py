def liste_des_mots(fichier: str) -> list:
    cleanup = ""
    mots_list = []
    with open(fichier) as f:
        contenu = f.read().lower()

    for c in contenu:
        if c.isalpha():
            cleanup += c
        else:
            cleanup += " "
    contenu = cleanup.split()

    for mot in sorted(contenu):
        if mot not in mots_list:
            mots_list.append(mot)
    return mots_list


print(
    liste_des_mots(
        "/Users/toots/Developer/computer-science/ULB/exercises/semaine-5/exercise-5.21/zola.txt"
    )
)
