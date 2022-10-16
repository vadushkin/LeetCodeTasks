class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()

        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)

        return pairs * 2 + 1 if unpaired_chars else pairs * 2


def main():
    s = Solution()
    print(s.longestPalindrome("abccccdd"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 42 ms, faster than 78.37% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.9 MB, less than 22.45% of Python3 online submissions for Longest Palindrome.

2. Runtime: 43 ms, faster than 76.13% of Python3 online submissions for Longest Palindrome.
Memory Usage: 14 MB, less than 22.45% of Python3 online submissions for Longest Palindrome.
"""
