class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1


def main():
    s = Solution()
    print(s.findLUSlength("aba", "cdc"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 55 ms, faster than 42.59% of Python3 online submissions for Longest Uncommon Subsequence I.
Memory Usage: 13.9 MB, less than 11.75% of Python3 online submissions for Longest Uncommon Subsequence I.

2. Runtime: 62 ms, faster than 17.89% of Python3 online submissions for Longest Uncommon Subsequence I.
Memory Usage: 13.9 MB, less than 58.77% of Python3 online submissions for Longest Uncommon Subsequence I.
"""
