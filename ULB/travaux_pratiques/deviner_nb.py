from random import randint
def deviner_nombre(nombre: int = None) -> None :
    if nombre != None :
        nb_secret = nombre
    else :
        nb_secret = randint(1, 100)
    while guess != nb_secret :
        guess = int(input())
        if guess > nb_secret :
            print("Your guess is too high")
        else:
            print("Your guess is too low")
            
    print(f"Well done it was {nb_secret}")
    