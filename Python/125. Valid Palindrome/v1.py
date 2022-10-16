class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isdigit() or c.isalpha())
        if s == s[::-1]:
            return True
        return False


def main():
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 75.87% of Python3 online submissions for Valid Palindrome.
Memory Usage: 19.1 MB, less than 11.36% of Python3 online submissions for Valid Palindrome.

2. Runtime: 85 ms, faster than 37.60% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.3 MB, less than 24.96% of Python3 online submissions for Valid Palindrome.
"""
