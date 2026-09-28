incrementation = int(input())
goal = int(input())
current = 0

while current != goal:
    current = (current + incrementation) % 100

    if current == goal:
        print("Cible atteinte")
        break

    print(current)

    if current == 0:
        print("Pas trouvée")
        break
