def couper(nombres: list, marqueur: int):
    if marqueur in nombres:
        for i in range(len(nombres)):
            if nombres[i] == marqueur:
                return nombres[:i], [nombres[i + 1 :]]
    else:
        return (nombres, [])


print(couper([-5, 7, 4, 10], 4))
print(couper([-5, 7, 4, 10], 42))
