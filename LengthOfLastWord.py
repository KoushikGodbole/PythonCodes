#did different submission in leetcode
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    t = s.split()
    if t == []:
        return 0
    else:
        return len(t[-1])


str = "   "
ret = lengthOfLastWord(str)
print(ret)
