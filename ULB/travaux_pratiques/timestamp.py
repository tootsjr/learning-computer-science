from time import time


def longue_fct():
    a = 0
    while a < 10000:
        a += 1
    return a


def timeit(f, n: int = 1000) -> float:
    total_time = 0
    for i in range(n):
        begin_t = time()
        f()
        end_time = time()
        total_time += end_time - begin_t
    return total_time / n


print(timeit(longue_fct, 100))
