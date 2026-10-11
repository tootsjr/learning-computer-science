def dupliques(sequence: list):

    for i in range(len(sequence)):
        if sequence[i] in sequence[i + 1 : len(sequence)]:
            return True
    return False
