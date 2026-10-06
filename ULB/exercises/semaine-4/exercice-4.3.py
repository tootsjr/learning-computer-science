def premier(n):
    for y in range(2, n + 1):
        if n == y:
            return True
        if n % y == 0:
            return False


n = int(input())
if premier(n):
    for i in range(n):
        if premier(i):
            print(i)
else:
    print(False)
