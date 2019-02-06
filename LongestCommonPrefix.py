def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    count = 0
    match = False
    if not strs:
        return ''
    shortest = min(strs, key=len)
    for i in range(len(shortest)):
        for subStr in strs:
            if shortest[i] == subStr[i]:
                match = True
            else:
                match = False
                break;
        if match:
            count += 1
        else:
            if i == 0:
                return ""
       # if sum(1 for s in strs if shortest[i] != s[i]) > 0:
       #     return shortest[:i]

    return shortest[:count]






strs = ["aa","ab"]
res = longestCommonPrefix(strs)
print(res)