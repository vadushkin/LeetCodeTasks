from itertools import groupby


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        return max((sum(g[1]) for g in groupby(nums) if g[0]), default=0)


def main():
    s = Solution()
    print(s.findMaxConsecutiveOnes([0, 1, 1, 0, 1, 1, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 706 ms, faster than 25.81% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.2 MB, less than 90.88% of Python3 online submissions for Max Consecutive Ones.

2. Runtime: 337 ms, faster than 98.96% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14 MB, less than 98.69% of Python3 online submissions for Max Consecutive Ones.
"""
