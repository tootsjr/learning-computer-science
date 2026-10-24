def trace(M):
    result = 0
    for i in range(len(M)):
        result += M[i][i]
    return result
