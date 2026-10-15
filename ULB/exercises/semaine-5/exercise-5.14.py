def distance_mots(mot_1: str, mot_2: str) -> int:
    similarities = 0
    for i in range(len(mot_1)):
        if mot_1[i] == mot_2[i]:
            similarities += 1
    return len(mot_1) - similarities
