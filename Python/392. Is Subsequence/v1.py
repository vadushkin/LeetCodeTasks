class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


def main():
    s = Solution()
    print(s.isSubsequence("342", "13452"))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 62 ms, faster than 27.15% of Python3 online submissions for Is Subsequence.
Memory Usage: 14 MB, less than 42.76% of Python3 online submissions for Is Subsequence.

2. Runtime: 71 ms, faster than 12.39% of Python3 online submissions for Is Subsequence.
Memory Usage: 14 MB, less than 12.66% of Python3 online submissions for Is Subsequence.
"""
