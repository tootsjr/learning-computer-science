n = int(input())


def cross(n):
    if n % 2 == 0:
        return
    for i in range(n // 2 + 1):
        x_extremites = "X" * i
        x_milieu = "X" * (n - 2 - 2 * i)
        if i == n // 2:
            print(x_extremites + "O" + x_extremites)
        else:
            print(x_extremites + "O" + x_milieu + "O" + x_extremites)

    for y in range(n // 2 - 1, -1, -1):
        x_extremites = "X" * y
        x_milieu = "X" * (n - 2 - 2 * y)
        print(x_extremites + "O" + x_milieu + "O" + x_extremites)


cross(n)

## OXXXO  for n = 5, the first 0 is first and the second is last
## XOXOX always n - 2 Xs and 2 0s except for the center
## XXOXX the center is n // 2
## XOXOX 0s position is for the first one: n + i (i being the i in the for loop), and for the second its n - i
## OXXXO
