x = int(input())
y = int(input())

# if x % y == 0 or y % x == 0:
#    print("False")
# else:
#    print("True")

print(not (x % y == 0 or y % x == 0))
