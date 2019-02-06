import itertools
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    keypad = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
               '9': 'wxyz'}
    combination = [keypad[d] for d in digits if d != '0' and d != '1']
    return [''.join(x) for x in itertools.product(*combination)]






num = 23
res = letterCombinations(str(num))
print(res)