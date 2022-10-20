class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        if s == s[::-1]:
            return True
        return False


def main():
    s = Solution()
    print(s.isPalindrome("123123123123321321321321"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 75.87% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.2 MB, less than 24.96% of Python3 online submissions for Valid Palindrome.

2. Runtime: 36 ms, faster than 99.43% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15 MB, less than 29.95% of Python3 online submissions for Valid Palindrome.

3. Runtime: 32 ms, faster than 99.82% of Python3 online submissions for Valid Palindrome. O_O
Memory Usage: 15.1 MB, less than 29.95% of Python3 online submissions for Valid Palindrome.
"""
