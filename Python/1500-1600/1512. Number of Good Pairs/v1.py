class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] == nums[j]:
                    ans += 1
        return ans


def main():
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 37 ms, faster than 90.23% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.8 MB, less than 95.93% of Python3 online submissions for Number of Good Pairs.

2. Runtime: 73 ms, faster than 14.80% of Python3 online submissions for Number of Good Pairs.
Memory Usage: 13.9 MB, less than 56.16% of Python3 online submissions for Number of Good Pairs.
"""
