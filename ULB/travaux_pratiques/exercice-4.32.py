def rotation(liste: list, n: int) -> list:
    result = []
    length = len(liste)

    for i in range(length):
        result.append(liste[(i + n) % length])

    return result


print(rotation([0, 1, 2, 3, 4, 5], 1))
print(rotation([0, 1, 2, 3, 4, 5], 3))
