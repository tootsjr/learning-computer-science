from math import pi


def aire_rectangle(longueur: float, largeur: float) -> float:
    return longueur * largeur


def aire_carre(cote: float) -> float:
    return aire_rectangle(cote, cote)  # return cote **2


def aire_triangle(base: float, hauteur: float) -> float:
    return aire_rectangle(base, hauteur / 2)


def aire_cercle(rayon: float) -> float:
    return pi * (aire_rectangle(rayon, rayon))
