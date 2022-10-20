class Solution(object):
    def romanToInt(self, s):
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            total = total + ((-1) ** (dict[s[i]] < dict[s[i + 1]])) * dict[s[i]]
        return total + dictionary[s[len(s) - 1]]


s = Solution()
print(s.romanToInt("III"))

"""Tests: 
1. Runtime: 52 ms, faster than 70.33% of Python online submissions for Roman to Integer.
Memory Usage: 13.5 MB, less than 30.90% of Python online submissions for Roman to Integer.

2. Runtime: 60 ms, faster than 55.38% of Python online submissions for Roman to Integer.
Memory Usage: 13.6 MB, less than 30.90% of Python online submissions for Roman to Integer.
"""
