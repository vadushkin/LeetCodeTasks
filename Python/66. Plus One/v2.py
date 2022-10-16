from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = ''.join([str(x) for x in digits])
        d = int(d) + 1
        out = [int(x) for x in str(d)]
        return out


s = Solution()
print(s.plusOne([1, 2, 3, 4]))

"""Tests:
1. Runtime: 37 ms, faster than 86.64% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 11.85% of Python3 online submissions for Plus One.

2. Runtime: 65 ms, faster than 16.44% of Python3 online submissions for Plus One.
Memory Usage: 13.8 MB, less than 96.68% of Python3 online submissions for Plus One.

3. Runtime: 69 ms, faster than 10.31% of Python3 online submissions for Plus One.
Memory Usage: 13.8 MB, less than 58.70% of Python3 online submissions for Plus One.
"""
