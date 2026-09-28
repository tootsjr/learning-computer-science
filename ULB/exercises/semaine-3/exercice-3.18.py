height = int(input())

for i in range(1, height + 1):
    print(" " * (height - i), end="")
    for y in range(
        i, 2 * i
    ):  # here we dont do 2i - 1 since the for loop is a strict < not a <=
        print(y % 10, end="")
    for n in range(
        2 * i - 2, i - 1, -1
    ):  # here we do -2 otherwise itll start off using the prior printed nnumber which was 2i -1
        print(n % 10, end="")

    print()
