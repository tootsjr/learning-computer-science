"""
this function is supposed to check if the first part of the word
appears at the end too
"""


def plus_grand_bord(w: str) -> str:
    # if you use a list the start is included the end is not -> we include len (second), and add one (first)
    bord = ""
    for i in range(len(w) - 1):
        if w[0 : i + 1] == w[len(w) - 1 - i : len(w)]:
            bord = w[0 : i + 1]
    return bord


print(plus_grand_bord("aaaaa"))
print(plus_grand_bord("abbbabbabbaba"))
