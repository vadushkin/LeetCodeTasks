class Solution:
    def isValid(self, s: str) -> bool:
        staples = s
        dict_staples = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        a = []
        if len(s) > 10000 or len(s) <= 1:
            return False
        for staple in staples:
            if staple in ['}', ')', ']'] and not a:
                return False
            elif not a:
                a.append(staple)
                continue
            else:
                a.append(staple)
                if a[-1] in ['}', ')', ']'] and a[-2] == dict_staples[staple]:
                    a.pop()
                    a.pop()
                elif a[-1] in ['}', ')', ']'] and a[-2] != dict_staples[staple]:
                    return False
                else:
                    continue
        if a:
            return False
        return True


s = Solution()
print(s.isValid("{}"))

"""Tests:
1. Runtime: 37 ms, faster than 83.03% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 25.50% of Python3 online submissions for Valid Parentheses.

2. Runtime: 33 ms, faster than 91.58% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 25.50% of Python3 online submissions for Valid Parentheses.
"""
