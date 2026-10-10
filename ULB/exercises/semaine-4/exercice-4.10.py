import random


def bat(seed: int) -> None:
    random.seed(seed)
    coups_list = ["Pierre", "Feuille", "Ciseaux"]
    score = 0
    for i in range(5):
        coup_j = int(input())
        coup_o = random.randint(0, 2)
        game = (coup_o + 1) % 3
        if coup_j == coup_o:
            print(f"{coups_list[coup_o]} annule {coups_list[coup_o]} : {score}")
        elif game == coup_j:
            score += 1
            print(f"{coups_list[coup_o]} est battu par {coups_list[coup_j]} : {score}")
        else:
            score -= 1
            print(f"{coups_list[coup_o]} bat {coups_list[coup_j]} : {score}")

    if score > 0:
        print("Gagné")
    elif score < 0:
        print("Perdu")
    else:
        print("Nul")


bat(int(input()))
