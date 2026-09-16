from math import sqrt

a = int(input("Enter a value for a : "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

if a != 0:
    delta = b**2 - 4 * a * c

    if delta < 0:
        print("No real solutions for this equation")

    elif delta == 0:
        print(f"Cela admet une solution solutions : {-b/(2*a)}")

    else:
        print(
            f"Cela admet 2 solutions : x1 = {(-b - sqrt(delta)) / (2*a)}, x2 = {(-b + sqrt(delta))/(2*a)} "
        )

else:
    print("a ne peut pas etre = 0")
