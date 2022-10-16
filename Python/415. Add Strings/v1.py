class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not (1 <= len(num1)) or not (len(num2) <= 10000):
            return ""
        return str(int(num2) + int(num1))


s = Solution()
print(s.addStrings('11', '100'))

"""Tests: 
1. Runtime: 39 ms, faster than 94.01% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 62.00% of Python3 online submissions for Add Strings.

2. Runtime: 62 ms, faster than 56.75% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 62.00% of Python3 online submissions for Add Strings.

3. Runtime: 47 ms, faster than 83.34% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 62.00% of Python3 online submissions for Add Strings.
"""