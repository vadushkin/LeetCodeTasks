from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        N = Counter(nums)
        return max([N[k] + N[k + 1] for k in list(N) if k + 1 in N] + [0])


def main():
    s = Solution()
    print(s.findLHS([1, 2, 3, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 364 ms, faster than 85.42% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 15.9 MB, less than 51.99% of Python3 online submissions for Longest Harmonious Subsequence.

2. Runtime: 797 ms, faster than 19.24% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 15.9 MB, less than 51.99% of Python3 online submissions for Longest Harmonious Subsequence.
"""
