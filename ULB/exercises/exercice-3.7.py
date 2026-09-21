pari = int(input())
tirage = int(input())

red_list = [1, 3, 5, 7, 9, 12]

if pari < 13:
    if pari == tirage:
        print(120)
    else:
        print(0)
elif pari == 13:
    if tirage % 2 == 0:
        print(20)
    else:
        print(0)
elif pari == 14:
    if tirage % 2 != 0:
        print(20)
    else:
        print(0)
elif pari == 15:
    if tirage in red_list:
        print(20)
    else:
        print(0)
elif pari == 16:
    if tirage in red_list:
        print(0)
    else:
        print(20)
