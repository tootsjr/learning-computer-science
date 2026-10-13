def modifie(liste):
    liste.append(4)


a = [1, 2, 3]
print(a, modifie(a))
"""
this returns the modified list and None, why? -> the function ALWAYS evals the params first
this only works though for mutable types (a mutable type is an object whose internal state 
or values can be modified after it is created without changing its identity (memory location)). 
And none since we are printing a function with no return
"""

# to actually print the correct, original list, then modified list, we need to create a second list.


def modifie_2(liste):
    r = liste[:]
    # list slicing, so it does not copy the address rather than the contents
    r.append(4)
    return r
