class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_str = len(haystack)
        if 1 > len_str or len_str > 104:
            return -1
        if needle in haystack:
            return haystack.index(needle)
        return -1


s = Solution()
print(s.strStr("hello", 'll'))

"""Tests:
1. Runtime: 48 ms, faster than 50.54% of Python3 online submissions for Implement strStr().
Memory Usage: 13.8 MB, less than 64.15% of Python3 online submissions for Implement strStr().

2. Runtime: 38 ms, faster than 77.77% of Python3 online submissions for Implement strStr().
Memory Usage: 13.8 MB, less than 97.27% of Python3 online submissions for Implement strStr().
"""
