import math

length = float(input())  # Gets the user's input as a flaot since all inputs are floats

for i in range(6):  # We iterate from 0 to 5 so 6 times for all sides of the shape
    angle_deg = i * 60  # We start off at 0 degrees then work our way up to 300
    x = math.cos(angle_deg * math.pi / 180) * length
    # to get the coords its cos(angle (for example 60) * pi / 180) * length
    y = math.sin(angle_deg * math.pi / 180) * length

    print(x, y)
