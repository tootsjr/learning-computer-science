def soleil_leve(lever, coucher, actuelle):
    if lever == coucher:
        return lever == 0
    elif lever > coucher:
        return actuelle <= coucher or actuelle >= lever
    return coucher > actuelle > lever
