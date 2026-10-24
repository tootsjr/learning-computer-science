# def print_mat(M):
#     """
#     This version is using returns, which is cleaner
#     """
#     result = ""
#     for i in range(len(M)):
#         for j in range(len(M[i])):
#             result += str(M[i][j]) + " "
#         result += "\n"
#     return result


def print_mat(M):
    """
    this version is using print
    """
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=" ")
        print()
    return 0


print_mat([["H", "E"], ["L", "L"], ["O", " "], ["W", "O"], ["R", "L"], ["D", "!"]])
