from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)


s = Solution()
print(s.superPow(1, [1, 2, 3, 4]))

"""Tests:
1. Runtime: 161 ms, faster than 55.96% of Python3 online submissions for Super Pow.
Memory Usage: 13.9 MB, less than 55.42% of Python3 online submissions for Super Pow.

2. Runtime: 178 ms, faster than 44.23% of Python3 online submissions for Super Pow.
Memory Usage: 14.1 MB, less than 24.19% of Python3 online submissions for Super Pow. 
"""
