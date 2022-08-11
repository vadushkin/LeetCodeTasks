class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        max_len = 1
        start = 0
        for i in range(len(s)):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:  # O_O
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]: # O_O
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]


s = Solution()
print(s.longestPalindrome("asdfghjkzxcvbnmmnbvcxzkjhgfsdaasdasdasdasd"))

"""Tests:
1. Runtime: 127 ms, faster than 98.92% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 60.50% of Python3 online submissions for Longest Palindromic Substring.

2. Runtime: 165 ms, faster than 98.05% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.1 MB, less than 29.52% of Python3 online submissions for Longest Palindromic Substring.
"""
