T = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]


def somme_col(M, j):
    s = 0
    for i in range(len(M)):
        s += M[i][j]
    return s


def somme_ligne(M, i):
    return sum(M[i])


def somme_diag(M):
    return sum(M[i][i] for i in range(len(M)))


def somme_diag_inverse(M):
    s = 0
    for i in range(len(M)):
        s += M[len(M) - i - 1][i]
    return s


def magique(M):

    n = len(M)
    res = True

    sdiag = somme_diag(M)
    sdiag_inverse = somme_diag_inverse(M)

    if sdiag != sdiag_inverse:
        res = False

    for i in range(n):
        if somme_ligne(M, i) != sdiag:
            res = False

    for j in range(n):
        scol = somme_col(M, j)
        if scol != sdiag:
            res = False

    return res


print(magique(T))
