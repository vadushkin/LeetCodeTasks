class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not (1 <= len(num1)) or not (len(num2) <= 200):
            return ""
        return str(int(num1) * int(num2))


s = Solution()
print(s.multiply('123', '123'))

"""Tests:
1. Runtime: 39 ms, faster than 91.71% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.9 MB, less than 74.98% of Python3 online submissions for Multiply Strings.

2. Runtime: 25 ms, faster than 99.72% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.9 MB, less than 31.13% of Python3 online submissions for Multiply Strings.

3. Runtime: 18 ms, faster than 99.98% of Python3 online submissions for Multiply Strings. O__O
Memory Usage: 13.9 MB, less than 74.98% of Python3 online submissions for Multiply Strings.
"""