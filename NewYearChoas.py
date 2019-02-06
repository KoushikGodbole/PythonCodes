def minimumBribes(q):
    count = 0
    for i in range(0, len(q)):
        if(q[i] != (i+1)):
            if(abs(q[i] - (i+1)) > 3):
                count = 99
                break
            count = count + abs(q[i] - (i+1))
            temp = q[i]
            q.remove(q[i])
            q.insert((temp-1),temp)
    return count

a  = [2, 5, 1, 3, 4]
res = minimumBribes(a)
if res == 99:
    print("Too chacotic\n")
else:
    print(res)