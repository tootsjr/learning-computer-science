i = 0
nombres = []
total = 0

while i != -1:
    i = int(input())
    if i != -1:
        nombres.append(i)

for y in nombres:
    total += y

moyenne = total / len(nombres)

print(moyenne)
