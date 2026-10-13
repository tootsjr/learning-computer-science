def distincs(elements: list) -> list:
    distincs_elements = []
    for c in elements:
        if c not in distincs_elements:
            distincs_elements.append(c)
    return distincs_elements
