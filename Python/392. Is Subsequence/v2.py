class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for c in s:
            i = t.find(c, start)
            if i == -1:
                return False
            start = i + 1
        return True


def main():
    s = Solution()
    print(s.isSubsequence('anbs', 'nsgsaadfnbwds'))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 41.51% of Python3 online submissions for Is Subsequence.
Memory Usage: 14 MB, less than 12.66% of Python3 online submissions for Is Subsequence.

2. Runtime: 54 ms, faster than 46.58% of Python3 online submissions for Is Subsequence.
Memory Usage: 13.9 MB, less than 42.76% of Python3 online submissions for Is Subsequence.
"""
