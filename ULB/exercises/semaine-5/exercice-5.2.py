def est_adn(adn: str) -> bool:
    if len(adn) < 1 :
        return False
    for i in range(len(adn)):
        if adn[i] != "A" and adn[i] != "C" and adn[i] != "G" and adn[i] != "T":
            return False
    return True
