def my_filter(lst: list, f) -> list:
    filtered_lst = []
    for c in lst:
        if f(c):
            filtered_lst.append(c)

    return filtered_lst


def est_pair(x):
    return x % 2 == 0


print(my_filter([1, 2, 3, 4, 5, 6], est_pair))
