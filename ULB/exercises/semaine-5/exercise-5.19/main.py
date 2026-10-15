def acrostiche(nom: str) -> str:
    with open(nom) as f:
        contents = f.read()
    result = contents[0]
    for i in range(len(contents) - 1):
        if contents[i] == "\n":
            result += contents[i + 1]

    return result


print(
    acrostiche(
        "/Users/toots/Developer/computer-science/ULB/exercises/semaine-5/exercise-5.10/text.txt"
    )
)
