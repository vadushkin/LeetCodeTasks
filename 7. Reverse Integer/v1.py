class Solution:
    def reverse(self, x: int) -> int:
        b = int(str(x)[::-1]) if str(x)[0] != "-" else int("-" + str(x)[::-1][:-1])
        if b >= 2 ** 31 - 1 or b <= -2 ** 31:
            return 0
        return b


s = Solution()
print(s.reverse(-1231231231231231231))

"""Tests:
1. Runtime: 35 ms, faster than 91.25% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 16.04% of Python3 online submissions for Reverse Integer.

2. Runtime: 33 ms, faster than 94.27% of Python3 online submissions for Reverse Integer. O_O
Memory Usage: 13.8 MB, less than 97.20% of Python3 online submissions for Reverse Integer.

3. Runtime: 42 ms, faster than 75.77% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 63.35% of Python3 online submissions for Reverse Integer.
"""
