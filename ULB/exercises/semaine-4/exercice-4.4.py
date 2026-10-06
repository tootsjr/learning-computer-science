import random


def alea_dice(s):
    random.seed(s)
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    dice_three = random.randint(1, 6)

    die = [dice_one, dice_two, dice_three]

    if 4 in die and 2 in die and 1 in die:
        return True
    else:
        return False


n = int(input())
print(alea_dice(n))
