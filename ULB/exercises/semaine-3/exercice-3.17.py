x = float(input())
sinus = 0
sign = -1  # starts off as -1, so we can then multiply by -1 to get one, to then swap each iteration
i = 0

while True:
    i += 1
    factoriel = 1  # starts at 1 otherwise we have a multiplication by 0 infinitly
    if i % 2 != 0:  # check if i is unpair
        sign = (
            sign * -1
        )  # changing sign after checking other wise it would always be negative
        for y in range(1, i + 1):  # to get the factoriel
            factoriel = factoriel * y
        sinus = sinus + sign * ((x**i) / factoriel)
        # print(factoriel)
        if abs((x**i) / factoriel) <= 10**-6:
            break

print(sinus)
