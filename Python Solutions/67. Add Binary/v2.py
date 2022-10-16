class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            summary = carry
            if i >= 0:
                summary += ord(a[i]) - ord('0')
            if j >= 0:
                summary += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if summary > 1 else 0
            res += str(summary % 2)

        if carry != 0: res += str(carry);
        return res[::-1]


s = Solution()
print(s.addBinary("1000", "1000"))

"""Tests:
1. Runtime: 40 ms, faster than 82.78% of Python3 online submissions for Add Binary.
Memory Usage: 14 MB, less than 24.71% of Python3 online submissions for Add Binary.

2. Runtime: 44 ms, faster than 73.78% of Python3 online submissions for Add Binary.
Memory Usage: 14 MB, less than 24.71% of Python3 online submissions for Add Binary.

3. Runtime: 37 ms, faster than 89.01% of Python3 online submissions for Add Binary.
Memory Usage: 13.9 MB, less than 24.71% of Python3 online submissions for Add Binary.
"""
