def soleil_leve(lever, coucher, actuelle):
    if lever == coucher:
        return lever == 0
    elif lever > coucher:
        return actuelle < coucher or actuelle >= lever
    return coucher > actuelle >= lever


def aurores(leverE1515, coucherE1515, leverE666, coucherE666):
    i = 0
    while i < 24:
        sun1_up = soleil_leve(leverE1515, coucherE1515, i)
        sun2_up = soleil_leve(leverE666, coucherE666, i)
        if sun1_up or sun2_up:
            print(i)
        else:
            print(i, "*")
        i += 1


aurores(int(input()), int(input()), int(input()), int(input()))
