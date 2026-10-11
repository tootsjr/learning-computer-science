def prime_numbers(nb: int):
    if type(nb) != int or nb < 0:
        return None
    premiers = []
    i = 2
    while len(premiers) < nb:
        if est_premier(i):
            premiers.append(i)
        i += 1
    return premiers


def est_premier(nb) -> bool:

    for i in range(2, nb):
        if nb % i == 0:
            return False
    return True


print(prime_numbers(0))
