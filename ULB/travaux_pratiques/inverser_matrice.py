def inverser(liste: list) -> None:
    item_temp = 0
    for i in range(len(liste) // 2):
        # liste[i], liste[-i - 1] = liste[-i - 1], liste[i] # without a temp veriable and in one line
        item_temp = liste[i]
        liste[i] = liste[-i - 1]
        liste[-i - 1] = item_temp


liste = [1, 2, 3, 4, 5]
inverser(liste)

print(liste)
