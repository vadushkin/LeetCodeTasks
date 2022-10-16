class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if len(needle) == 0:
            return 0
        else:
            for number in range(0, int(len(haystack) - len(needle)) + 1):
                if haystack[number:number + len(needle)] == needle:
                    index = number
                    break
        return index


s = Solution()
print(s.strStr("hello", "hello"))


"""Tests: 
1. Runtime: 42 ms, faster than 67.12% of Python3 online submissions for Implement strStr().
Memory Usage: 13.8 MB, less than 64.15% of Python3 online submissions for Implement strStr().

2. Runtime: 39 ms, faster than 74.86% of Python3 online submissions for Implement strStr().
Memory Usage: 13.9 MB, less than 15.38% of Python3 online submissions for Implement strStr().
"""