def antisymetrique(M) -> bool:
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != -(M[j][i]):
                return False
    return True
