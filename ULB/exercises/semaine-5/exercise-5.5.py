from math import sqrt


def longueur(*points):
    length = 0
    for i in range(0, len(points) - 1):
        length += sqrt(
            (points[i + 1][0] - points[i][0]) ** 2
            + (points[i + 1][1] - points[i][1]) ** 2
        )

    return length
