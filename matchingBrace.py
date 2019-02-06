def braces(values):
    i,j = -1, 0
    while j < len(values):
        if ((i == -1) or (not match(values, i, j))):
            i += 1
            value[i] = values[j]
            j += 1
        else:
            i -= 1
            j += 1

    return i == -1


def match(values, i ,j):
    if ((values[i] == '(' and values[j] == ')') or (values[i] == '[' and values[j] == ']') or (values[i] == '{' and values[j] == '}')):
        return True
    return False





res = braces("([)]{}")
print(res)

