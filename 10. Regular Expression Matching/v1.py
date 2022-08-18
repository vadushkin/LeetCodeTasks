import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.search(f"^{p}$", s) is not None


s = Solution()
print(s.isMatch("aab", "c*a*b" ))
"""Tests:
1. Runtime: 81 ms, faster than 53.80% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14 MB, less than 62.52% of Python3 online submissions for Regular Expression Matching.

2. Runtime: 86 ms, faster than 48.91% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14 MB, less than 38.71% of Python3 online submissions for Regular Expression Matching.
"""