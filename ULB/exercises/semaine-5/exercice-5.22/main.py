def wc(fileName) -> tuple:
    with open(fileName) as f:
        content = f.read()
    nb_chars = len(content)
    nb_words = len("".join(c if c.isalnum() else " " for c in content).split())
    # start off with an empty string and joins c if it is alnum otherwise we add a space to then be able to split each space into a word
    # [expression for variable in sequence if condition]
    nb_lines = len(content.split("\n")) - 1

    return (nb_chars, nb_words, nb_lines)


print(wc("exercises/semaine-5/exercice-5.22/petit-prince.txt"))
