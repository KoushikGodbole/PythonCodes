def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    example = s
    temp_len = len(example)
    count, i , max_len = 0, 0, 0
    temp_dict = dict()
    while (i < temp_len):
        if (ord(example[i]) in temp_dict):
            temp = temp_dict[ord(example[i])]
            temp_dict.clear()
            i = temp + 1
            if (max_len < count):
                max_len = count
            count = 0
        else:
            temp_dict[ord(example[i])] = i
            count = count + 1
            i += 1

    if (max_len < count):
        max_len = count
    return max_len


res = lengthOfLongestSubstring("abcabcabcbb")
print(res)