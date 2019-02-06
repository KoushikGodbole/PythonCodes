def solution(A):
    ex= {}
    maximum, left = 0,0
    for i in range(0, len(A)):
        if(A[i] in ex.keys()):
            ex[A[i]] += 1
        else:
            ex[A[i]] = 1

        while(len(ex) > 2):
            if(ex[A[left]] == 1):
                del ex[A[left]]
            else:
                ex[A[left]] -= 1
            left += 1

        maximum = max(maximum,(i- left + 1))


    return maximum









A = [1, 2, 1, 2, 1, 2, 1]
res = solution(A)
print(res)