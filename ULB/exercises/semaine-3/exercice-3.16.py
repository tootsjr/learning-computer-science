n = int(input())

for i in range(1, n + 1):
    for y in range(1, n + 1):
        print(y * i, end="\t")
    print("\n")
