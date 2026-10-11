"""Verifier une bijectivite entre deux strings"""


def anagrammes(v, w):
    copy_w = list(
        w
    )  # str in py != str in cpp, need to convert to list to be able to .remove
    for c in v:
        if c in copy_w:
            copy_w.remove(c)
        else:
            return False
    return True
