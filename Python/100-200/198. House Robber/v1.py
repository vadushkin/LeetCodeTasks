class Solution:
    def rob(self, nums: list[int]) -> int:
        count = len(nums)

        if count == 0:
            return 0
        elif count == 1:
            return nums[0]
        elif count == 2:
            return max(nums[0], nums[1])

        memo = nums[:]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, count):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])

        return memo[count - 1]


def main():
    s = Solution()
    print(s.rob([1, 2, 3, 1]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 30 ms Beats 96.26%
   Memory 13.9 MB Beats 66.57%

2. Runtime 31 ms Beats 94.97%
   Memory 13.9 MB Beats 66.57%
"""
