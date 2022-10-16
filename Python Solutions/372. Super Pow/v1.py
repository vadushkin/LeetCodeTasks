from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join([str(i) for i in b])), 1337)


s = Solution()
print(s.superPow(1, [4, 3, 3, 8, 5, 2]))

"""Tests:
1. Runtime: 171 ms, faster than 48.56% of Python3 online submissions for Super Pow.
Memory Usage: 13.9 MB, less than 55.42% of Python3 online submissions for Super Pow.

2. Runtime: 177 ms, faster than 44.95% of Python3 online submissions for Super Pow.
Memory Usage: 14.1 MB, less than 24.19% of Python3 online submissions for Super Pow.
"""