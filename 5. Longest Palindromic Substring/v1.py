class Solution:
    def longestPalindrome(self, s: str) -> str:
        if 1 > len(s) or len(s) > 1000:
            return ""
        if s == s[::-1]:
            return s
        palindromic = ""
        for e in range(len(s)):
            for i in range(1, len(s) + 1):
                if s[e:i] == s[e:i][::-1]:
                    if len(s[e:i]) > len(palindromic):
                        palindromic = s[e:i]
        return palindromic


s = Solution()
print(s.longestPalindrome("asddsad"))

"""Tests:
1. Runtime: 953 ms, faster than 82.25% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 60.50% of Python3 online submissions for Longest Palindromic Substring.

2. Runtime: 579 ms, faster than 92.01% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.8 MB, less than 91.35% of Python3 online submissions for Longest Palindromic Substring.
"""
