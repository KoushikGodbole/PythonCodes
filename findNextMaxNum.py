

def formNumber(llval):
    i, res = 0,0
    while i < len(llval):
        res = res * 10 + llval[i]
        i += 1
    return res

def findNextMax(num):
    temp = [int(i) for i in str(num)]
    i = len(temp) - 1
    while i >= 1:
        if temp[i] > temp[i-1]:
            temp[i], temp[i-1] = temp[i-1], temp[i]
            break
        else:
            i -= 1
    if i > 0:
        res = formNumber(temp)
    else:
        res = 0
    return res


res = findNextMax(206155)
if res :
    print(res)
else:
    print("Next highest number cann't be found")