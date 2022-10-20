class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        n = len(word)
        match1, match2, match3 = True, True, True

        for i in range(n):
            if not word[i].isupper():
                match1 = False
                break
        if match1:
            return True

        for i in range(n):
            if word[i].isupper():
                match2 = False
                break
        if match2:
            return True

        if not word[0].isupper():
            match3 = False

        if match3:
            for i in range(1, n):
                if word[i].isupper():
                    match3 = False
        if match3:
            return True

        return False


def main():
    s = Solution()
    print(s.detectCapitalUse("USA"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 37.76% of Python3 online submissions for Detect Capital.
Memory Usage: 13.8 MB, less than 58.44% of Python3 online submissions for Detect Capital.

2. Runtime: 31 ms, faster than 96.05% of Python3 online submissions for Detect Capital.
Memory Usage: 13.9 MB, less than 10.04% of Python3 online submissions for Detect Capital.
"""
