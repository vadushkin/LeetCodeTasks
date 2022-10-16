class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        return [word for word in words if
                all(w.lower() in "qwertyuiop" for w in word) or
                all(w.lower() in "asdfghjkl" for w in word) or
                all(w.lower() in "zxcvbnm" for w in word)]


def main():
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 63 ms, faster than 19.26% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.9 MB, less than 16.84% of Python3 online submissions for Keyboard Row.

2. Runtime: 72 ms, faster than 6.36% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.9 MB, less than 16.84% of Python3 online submissions for Keyboard Row.

3. Runtime: 37 ms, faster than 84.16% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.8 MB, less than 68.26% of Python3 online submissions for Keyboard Row.
"""
