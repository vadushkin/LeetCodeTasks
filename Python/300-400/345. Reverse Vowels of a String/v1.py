import re


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


def main():
    s = Solution()
    print(s.reverseVowels("hello"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 120 ms, faster than 33.44% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 16.1 MB, less than 14.63% of Python3 online submissions for Reverse Vowels of a String.

2. Runtime: 109 ms, faster than 42.08% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 16 MB, less than 15.70% of Python3 online submissions for Reverse Vowels of a String.
"""
