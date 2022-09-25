import collections


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x + 1 in count:
                ans = max(ans, count[x] + count[x + 1])
        return ans


def main():
    s = Solution()
    print(s.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 302 ms, faster than 99.13% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 16 MB, less than 51.99% of Python3 online submissions for Longest Harmonious Subsequence.

2. Runtime: 299 ms, faster than 99.42% of Python3 online submissions for Longest Harmonious Subsequence.
Memory Usage: 15.9 MB, less than 51.99% of Python3 online submissions for Longest Harmonious Subsequence.
"""
