class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if 1 > len(a) or len(b) > 10000:
            return ''
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
print(s.addBinary('1000', '1'))


"""Tests:
1. Runtime: 35 ms, faster than 92.38% of Python3 online submissions for Add Binary.
Memory Usage: 13.9 MB, less than 24.71% of Python3 online submissions for Add Binary.

2. Runtime: 50 ms, faster than 58.78% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 72.75% of Python3 online submissions for Add Binary.

3. Runtime: 37 ms, faster than 89.01% of Python3 online submissions for Add Binary.
Memory Usage: 13.9 MB, less than 24.71% of Python3 online submissions for Add Binary.
"""