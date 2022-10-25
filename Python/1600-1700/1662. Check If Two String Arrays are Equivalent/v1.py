class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


def main():
    s = Solution()
    print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 52 ms, faster than 68.58% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.8 MB, less than 75.82% of Python3 online submissions for Check If Two String Arrays are Equivalent. 

2. Runtime: 59 ms, faster than 52.41% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.9 MB, less than 33.11% of Python3 online submissions for Check If Two String Arrays are Equivalent.
"""
