import random

NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
guess = 0

while True:
    guess = int(input())
    NB_ESSAIS_MAX -= 1

    if guess == secret:
        print(f"Gagné en {6 - NB_ESSAIS_MAX} essai(s) !")
        break

    if NB_ESSAIS_MAX == 0:
        print(f"Perdu ! Le secret était {secret}")
        break

    if guess > secret:
        print("Trop grand")

    elif guess < secret:
        print("Trop petit")
