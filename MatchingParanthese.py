def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    result = []
    for s in values:
        i = 0
        stack = []
        size = len(s)
        valid = False
        if (size == 0):
            return True
        while (i < size):
            if (s[i] == '{' or s[i] == '[' or s[i] == '('):
                stack.append(s[i])
            elif (s[i] == ')'):
                if ((len(stack) != 0) and ('(' == stack.pop())):
                    valid = True
                else:
                    valid = False
                    break
            elif (s[i] == ']'):
                if ((len(stack) != 0) and ('[' == stack.pop())):
                    valid = True
                else:
                    valid = False
                    break
            elif (s[i] == '}'):
                if ((len(stack) != 0) and ('{' == stack.pop())):
                    valid = True
                else:
                    valid = False
                    break
            elif (len(stack) != 0):
                valid = False
            else:
                valid = False
            i += 1

        if (len(stack) != 0):
            valid = False
        if valid:
            result.append('YES')
        else:
            result.append('NO')

    return '\n'.join(result)



res = isValid("{}[]()\n{[}]")
print(res)