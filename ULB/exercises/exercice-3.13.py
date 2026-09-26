quantite = int(input())
nombres = 0
unit = 0

if quantite > 0:
    for i in range(quantite):
        nombres += int(input())
else:
    while True:
        unit = input()
        if unit != "F":
            nombres += int(unit)
        else:
            break
print(nombres)
