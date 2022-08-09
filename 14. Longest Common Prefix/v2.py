from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = min(strs)
        for i in range(len(strs)):

            for j in range(len(res)):
                if strs[i][j] != res[j]:
                    res = res[:j]
                    break
        return res


s = Solution()
print(s.longestCommonPrefix(["fl", "fl", "fl"]))

"""Tests: 
1. Runtime: 62 ms, faster than 33.51% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 12.01% of Python3 online submissions for Longest Common Prefix.

2. Runtime: 44 ms, faster than 76.59% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 50.09% of Python3 online submissions for Longest Common Prefix.
"""