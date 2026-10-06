n = int(input())

prec = 0
succ = 1
print(f"{prec}\n{succ}")

for i in range(n - 2):
    prec_temp = prec
    prec = succ
    succ = prec_temp + succ
    print(prec, " ", succ)
