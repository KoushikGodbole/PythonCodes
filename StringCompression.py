def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    right, left = 0, 0
    while right < len(chars):
        match, count = chars[right], 0
        while right < len(chars) and chars[right] == match:
            right, count = right + 1, count + 1
        chars[left], left = match, left + 1
        if count > 1:
                chars[left], left = str(count), left + 1
    return left


temp = ["b","b","b","b","b","b","a"]
res = compress(temp)
print(res)
