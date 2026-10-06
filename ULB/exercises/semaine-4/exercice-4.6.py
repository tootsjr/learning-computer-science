"""we need to be able to have a and b at default values of a = 0, and b = 1,
and can be changed by user input"""


def somme(a=0, b=1):  # has a default value of 0 and 1 if none are inputed
    somme = a + b
    return somme


a = 0
b = 1
somme(a, b)
