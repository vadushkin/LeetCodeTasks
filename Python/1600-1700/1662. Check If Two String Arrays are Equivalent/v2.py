class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True

    def generate(self, wordlist: list[str]):
        for word in wordlist:
            for char in word:
                yield char
        yield None


def main():
    s = Solution()
    print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 70 ms, faster than 16.21% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 14 MB, less than 33.11% of Python3 online submissions for Check If Two String Arrays are Equivalent.

2. Runtime: 55 ms, faster than 62.71% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 14 MB, less than 33.11% of Python3 online submissions for Check If Two String Arrays are Equivalent.
"""
