from math import sqrt


def distance_points(x: tuple, y: tuple):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
