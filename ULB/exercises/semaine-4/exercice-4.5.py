def rendre_monnaie(prix, vingt, dix, cinq, deux, un):
    argent = vingt * 20 + dix * 10 + cinq * 5 + deux * 2 + un
    billets = [20, 10, 5, 2, 1]
    rendu = argent - prix
    rendu_billet = [0] * 5
    y = 0
    if rendu == 0:
        return 0, 0, 0, 0, 0
    elif rendu < 0:
        return None, None, None, None, None
    for i in billets:
        rendu_billet[y] = rendu // i
        rendu -= rendu_billet[y] * i
        print(rendu)
        y += 1
    return (*rendu_billet,)


print(
    rendre_monnaie(
        int(input()),
        int(input()),
        int(input()),
        int(input()),
        int(input()),
        int(input()),
    )
)
