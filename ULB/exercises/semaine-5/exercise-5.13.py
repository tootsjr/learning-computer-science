def my_insert(liste_croissante: list, n: int):
    i = 0
    if type(n) != int:
        raise AssertionError
    else:
        return_status = None
    while i < (len(liste_croissante)) and liste_croissante[i] < n:
        i += 1

    liste_croissante.insert(i, n)

    return return_status


print(my_insert([0, 1, 2, 3, 3, 4, 4], 5))
