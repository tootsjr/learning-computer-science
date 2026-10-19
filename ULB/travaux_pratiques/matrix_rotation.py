def nouvelle_matrice(n):
    M = []
    for i in range(n):
        M.append([0] * n)
    return M


def ratation(M):
    n = len(M)
    R = nouvelle_matrice(n)
    for i in range(n):
        for j in range(n):
            R[j][n - 1 - i] = M[i][j]
