from math import sqrt

premiere_lettre = input()
premiere_lettre = premiere_lettre[0].upper()

a = float(input())

if premiere_lettre == "T":
    print((sqrt(2) / 12) * a**3)
elif premiere_lettre == "C":
    print(a**3)
elif premiere_lettre == "O":
    print((sqrt(2) / 3) * a**3)
elif premiere_lettre == "D":
    print(((15 + 7 * sqrt(5)) / 4) * a**3)
elif premiere_lettre == "I":
    print((5 * (3 + sqrt(5)) / 12) * a**3)
else:
    print("Polyèdre non connu")
