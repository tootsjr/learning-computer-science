import math


def rac_eq_2nd_deg(a: float, b: float, c: float) -> tuple:
    delta = b**2 - 4 * a * c
    if delta == 0:
        return (-b / (2 * a), )
    elif delta > 0:
        x_1, x_2 = (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a),
        if x_1 > x_2 :
            return (x_2, x_1)
        else:
            return (x_1, x_2)            
    else : 
        return ()


print(rac_eq_2nd_deg(float(input()), float(input()), float(input())))