class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word[0].islower() and word[1:].islower():
            return True

        if word.upper() == word:
            return True

        if word.lower() == word:
            return True

        return False


def main():
    s = Solution()
    print(s.detectCapitalUse("USA"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 35 ms, faster than 90.51% of Python3 online submissions for Detect Capital.
Memory Usage: 13.8 MB, less than 58.44% of Python3 online submissions for Detect Capital.

2. Runtime: 63 ms, faster than 27.22% of Python3 online submissions for Detect Capital.
Memory Usage: 13.8 MB, less than 58.44% of Python3 online submissions for Detect Capital.
"""
