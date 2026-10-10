from math import sqrt


def somme_carre(a: float, b: float) -> float:
    return (a + b) ** 2


def diff_carre(a: float, b: float) -> float:
    return somme_carre(a, -b)


def diff_carres(a: float, b: float) -> float:
    return a**2 - b**2
