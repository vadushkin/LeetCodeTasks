class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''

        for i in range(n // 2):

            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'


def main():
    s = Solution()
    print(s.breakPalindrome("aba"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 65 ms, faster than 13.31% of Python3 online submissions for Break a Palindrome.
Memory Usage: 14 MB, less than 13.13% of Python3 online submissions for Break a Palindrome.

2. Runtime: 63 ms, faster than 17.76% of Python3 online submissions for Break a Palindrome.
Memory Usage: 13.9 MB, less than 61.62% of Python3 online submissions for Break a Palindrome.
"""
