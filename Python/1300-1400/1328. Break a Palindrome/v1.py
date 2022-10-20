class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome) - 1):
            for j in range(ord('a'), ord(palindrome[i])):
                string = palindrome[:i] + chr(j) + palindrome[i + 1:]
                if string != string[::-1]:
                    return string
        for j in range(ord('a'), ord('z')):
            string = palindrome[:-1] + chr(j)
            if string != string[::-1]:
                return string
        return ""


def main():
    s = Solution()
    print(s.breakPalindrome("aba"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 32 ms, faster than 92.92% of Python3 online submissions for Break a Palindrome.
Memory Usage: 13.8 MB, less than 61.62% of Python3 online submissions for Break a Palindrome.

2. Runtime: 52 ms, faster than 52.54% of Python3 online submissions for Break a Palindrome.
Memory Usage: 14 MB, less than 13.13% of Python3 online submissions for Break a Palindrome.
"""
