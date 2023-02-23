class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_helper(_nums):
            dp1, dp2 = 0, 0

            for num in _nums:
                dp1, dp2 = dp2, max(dp1 + num, dp2)

            return dp2

        return max(nums[0] + rob_helper(nums[2:-1]), rob_helper(nums[1:]))


def main():
    s = Solution()
    print(s.rob([1, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 38 ms Beats 39.87% 
   Memory 13.9 MB Beats 62.36%

2. Runtime 31 ms Beats 81.70% 
   Memory 13.9 MB Beats 62.36%
"""
