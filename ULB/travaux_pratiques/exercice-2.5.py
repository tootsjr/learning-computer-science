a = int(input())
b = int(input())

if a < 0 or b < 0:
    print("Erreur")
else:
    if a % b == 0 or b % a == 0:
        print("True")
    else:
        print("a et b ne sont pas multiples l’un de l’autre")
