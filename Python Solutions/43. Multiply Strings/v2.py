class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # fors :))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        res1, res2 = 0, 0
        for d in num1:
            res1 = res1 * 10 + (ord(d) - ord('0'))
        for d in num2:
            res2 = res2 * 10 + (ord(d) - ord('0'))
        return str(res1 * res2)


s = Solution()
print(s.multiply('123', '123'))
"""Tests: 
1. Runtime: 68 ms, faster than 59.32% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.9 MB, less than 74.98% of Python3 online submissions for Multiply Strings.

2. Runtime: 55 ms, faster than 72.13% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.9 MB, less than 31.13% of Python3 online submissions for Multiply Strings
"""
