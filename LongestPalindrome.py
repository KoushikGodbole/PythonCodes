def longestPalindrome(s):
    if s is None or len(s) == 0:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        length = max(len1, len2)

        if length > (end - start):
            start = i - ((length - 1) // 2)
            end = i + ((length) // 2)

    return s[start:end + 1]


def expandAroundCenter(s, left, right):
    l = left
    r = right
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    # print(r,l)
    # print(s[r],s[l])
    return r - l - 1



input = "babad"
res = longestPalindrome(input)
print(res)