def joindre(seperator: str, mots: list) -> str:
    modifier = ""
    times = 0
    for c in mots:
        modifier += seperator * times + c
        times = 1

    return modifier


print(joindre("--", ["Salut", "je programme", "en python"]))
