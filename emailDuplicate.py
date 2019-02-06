def solution(L):
    ex = {}
    for i in range(0, len(L) - 1):
        str = L[i].split('@')
        value = ""
        for j in range(0,len(str) -1):
            if(str[0][j] != '+'):
                if(str[0][j] != '.'):
                    value = value + str[0][j]
                else:
                    break


        key = value + '@' + str[1]
        if(key in ex.keys()):
            ex[key] = ex[key] + 1
        else:
            ex[key] = 1

    result = 0
    for (key,val) in ex.items():
        if (val > 1):
            result += 1


    return result




test = ["a.b@example.com", "x@example.com", "x@exa.mple.com",
                "ab+1@example.com", "y@example.com", "y@example.com","y@example.com",
                "y@exam.ple.com", "y+1111@exam.ple.com", "y+111@exam.ple.com"]
res = solution(test)
print(res)