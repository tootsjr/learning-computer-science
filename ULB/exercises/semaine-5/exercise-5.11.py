def intersection(v: str, w: str) -> str:
    found_intersection = ""
    temp_intersection = ""
    for i in range(len(v)):
        if v[i] in w:
            for j in range(i, len(v)):
                if v[i : j + 1] in w:
                    temp_intersection = v[i : j + 1]
                else:
                    break

        if len(temp_intersection) > len(found_intersection):
            found_intersection = temp_intersection
            temp_intersection = ""

    return found_intersection


print(intersection("programme", "grammaire"))
print(intersection("police", "picole"))
