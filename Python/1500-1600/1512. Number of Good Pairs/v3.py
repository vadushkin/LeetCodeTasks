import collections


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum(int(k * (k - 1) // 2) for k in collections.Counter(nums).values())


def main():
    s = Solution()
    print(s.numIdenticalPairs([1, 1, 1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 42.10% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.8 MB, less than 56.16% of Python3 online submissions for Number of Good Pairs.

2. Runtime: 60 ms, faster than 42.10% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.8 MB, less than 56.16% of Python3 online submissions for Number of Good Pairs.
"""
