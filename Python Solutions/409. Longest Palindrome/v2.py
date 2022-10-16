import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)


def main():
    s = Solution()
    print(s.longestPalindrome("qweqweqweqweqweqwe"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 49 ms, faster than 62.92% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.9 MB, less than 22.45% of Python3 online submissions for Longest Palindrome.

2. Runtime: 37 ms, faster than 88.27% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.8 MB, less than 66.76% of Python3 online submissions for Longest Palindrome.
"""
