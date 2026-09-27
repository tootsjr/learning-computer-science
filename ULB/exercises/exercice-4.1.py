x, y, z = int(input()), int(input()), int(input())


def deux_egaux(a, b, c):
    return a == b or b == c or a == c


print(deux_egaux(x, y, z))
