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
