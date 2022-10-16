# this is a max score in the entire list
# class Solution:
#     def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
#         ans = []
#         for i in range(len(multipliers)):
#             max_n = max(nums)
#             min_n = min(nums)
#             max_m = max(multipliers)
#             min_m = min(multipliers)
#             if max_n * max_m > min_n * min_m:
#                 ans.append(max_n * max_m)
#                 nums.remove(max_n)
#                 multipliers.remove(max_m)
#             else:
#                 ans.append(min_n * min_m)
#                 nums.remove(min_n)
#                 multipliers.remove(min_m)
#         return ans

# Brute Force
# class Solution:
#     def maximumScore(self, nums, multipliers):
#         m = len(multipliers)
#
#         def helper(nums, op):
#             if op == m:
#                 return 0
#             return max(nums[0] * multipliers[op] + helper(nums[1:], op + 1),
#                        nums[-1] * multipliers[op] + helper(nums[:-1], op + 1))
#
#         return helper(nums, 0)
# Time Limit Error

# class Solution:
#     def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
#         m = len(multipliers)
#         n = len(nums)
#         memo = {}
#
#         def dp(op, left):
#             if op == m:
#                 return 0
#             if (op, left) in memo:
#                 return memo[(op, left)]
#             l = nums[left] * multipliers[op] + dp(op + 1, left + 1)
#             r = nums[(n - 1) - (op - left)] * multipliers[op] + dp(op + 1, left)
#             memo[(op, left)] = max(l, r)
#             return memo[(op, left)]
#
#         return dp(0, 0)
# Time Limit Error

class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]


def main():
    s = Solution()
    print(s.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 8767 ms, faster than 28.57% Python3 for Maximum Score from Performing Multiplication Operations.
Memory Usage: 41.1 MB, less than 47.52% Python3 for Maximum Score from Performing Multiplication Operations.

2. Runtime: 9265 ms, faster than 15.04% Python3 for Maximum Score from Performing Multiplication Operations.
Memory Usage: 40.1 MB, less than 77.46% Python3 for Maximum Score from Performing Multiplication Operations.
"""
