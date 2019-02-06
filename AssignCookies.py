def findContentChildren(g: 'List[int]', s: 'List[int]'):
    count = 0
    g.sort()
    s.sort()
    i, j, count = 0, 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
            count += 1
        j += 1
    return count



g = [10,9,8,7]
s= [5,6,7,8]
res = findContentChildren(g,s)
print(res)