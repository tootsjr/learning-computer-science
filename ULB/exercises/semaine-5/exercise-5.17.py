def decompresse(liste: list) -> list:
    t = []
    for i in range(len(liste)):
        n = liste[i][0]
        x = liste[i][1]
        for y in range(n):
            t.append(x)
    return t

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))
