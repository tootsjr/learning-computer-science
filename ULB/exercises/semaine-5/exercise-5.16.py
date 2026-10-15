def my_pow(m: int, b: float):
    if type(m) != int or type(b) != float:
        return None
    list_powers = [b**i for i in range(m)]

    return list_powers


print(my_pow(3, 5.0))
