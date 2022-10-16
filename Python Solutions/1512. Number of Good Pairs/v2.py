class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return sum([1 if nums[i] == nums[j] else 0 for i in range(len(nums) - 1) for j in range(i + 1, len(nums))])


def main():
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 34 ms, faster than 94.33% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.8 MB, less than 56.16% of Python3 online submissions for Number of Good Pairs.

2. Runtime: 64 ms, faster than 32.30% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.8 MB, less than 56.16% of Python3 online submissions for Number of Good Pairs.
"""
