def est_adn(chaine: str) -> bool:
    """
    Verifies if the inputed string only contains A, C, G or T and is not empty.

    :param chaine : String to check.

    :return : Of type bool, whether the chain is purely A, C, G or T or not.
    """

    adn = "ACGT"
    result = True
    if len(chaine) < 1:
        result = False

    for c in chaine:
        if not c in adn:
            result = False

    return result


print(est_adn("ATGGT"))
print(est_adn("CTaG"))
print(est_adn(""))
