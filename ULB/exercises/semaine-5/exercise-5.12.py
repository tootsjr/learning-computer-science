def my_insert(liste_croissante: list, n: int):
    i = 0
    if type(n) != int:
        return None
    while i < (len(liste_croissante)) and liste_croissante[i] < n:
        i += 1

    return liste_croissante[0:i] + [n] + liste_croissante[i:]


print(my_insert([0, 1, 2, 3, 3, 4, 4], 5))
