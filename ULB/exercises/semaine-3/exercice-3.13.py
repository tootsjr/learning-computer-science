quantite = int(input())
nombres = 0
unit = 0

if quantite > 0:
    for i in range(quantite):  # quand tu sais combien de fois tu va repete
        nombres += int(input())
else:
    while True:  # quand tu ne sais pas le nombre de fois tu repete
        unit = input()
        if unit != "F":
            nombres += int(unit)
        else:
            break
print(nombres)
