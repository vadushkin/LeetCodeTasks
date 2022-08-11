# from collections import defaultdict
# def is_unique3(s):
#     dd = defaultdict(bool)
#     for char in s:
#         if dd[char]:
#             return False
#         dd[char] = True
#     return True


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if 0 > len(s) or len(s) > 50000:
            return 0
        down_str = ""
        for f in range(0, len(s) - 1):
            for i in range(len(s)):
                if s[f:i] in s[f + 1:] and s[f:i] != "" and len(down_str) < len(s[f:i]):
                    # if is_unique3(s[f:i]):
                    down_str = s[f:i]
        return len(down_str)


s = Solution()
print(s.lengthOfLongestSubstring("aaaa"))

"""Work with Repeating Characters"""


"""Tests:
1. O_O

2. O_O
"""