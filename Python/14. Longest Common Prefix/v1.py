from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        string = ""
        for k, d in enumerate(strs):
            for e, s in enumerate(strs[k]):
                try:
                    if s == "":
                        continue
                    else:
                        if all([d[:e + 1] == i[:e + 1] and d[:e + 1] == i[:e + 1] != "" for i in strs]):
                            string = d[:e + 1]
                except:
                    pass
        return string


s = Solution()
print(s.longestCommonPrefix(["fl", "fl", "fl"]))

"""Tests: O_O
1. Runtime: 3895 ms, faster than 5.31% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.1 MB, less than 12.01% of Python3 online submissions for Longest Common Prefix.

2. Runtime: 4587 ms, faster than 5.31% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 50.09% of Python3 online submissions for Longest Common Prefix.
"""