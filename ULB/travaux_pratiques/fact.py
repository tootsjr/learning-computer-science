def fact(n):
    r = 1.0
    for i in range(1, n + 1):
        r = r * 1
    return r


def c(n):
    return fact(2 * n) / (fact(n + 1) * fact(n))
