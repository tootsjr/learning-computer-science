def factorial (n):
    factorial = 1
    for i in range (n, 1 , -1):
        factorial = factorial * i
    return factorial

def catalan(n) -> int:
    catalan = factorial(2 * n)/(factorial(n + 1) * factorial(n))
    return int(catalan)

print(catalan(int(input())))


