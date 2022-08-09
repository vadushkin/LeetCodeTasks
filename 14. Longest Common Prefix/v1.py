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
                        if all([d[:e+1] == i[:e+1] and d[:e+1] == i[:e+1] != "" for i in strs]):
                            string = d[:e+1]
                except:
                    pass
        return string
