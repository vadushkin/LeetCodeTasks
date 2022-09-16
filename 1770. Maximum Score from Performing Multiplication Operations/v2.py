class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            nextRow = dp.copy()
            for left in range(i, -1, -1):
                dp[left] = max(multipliers[i] * nums[left] + nextRow[left + 1],
                               multipliers[i] * nums[n - 1 - (i - left)] + nextRow[left])
        return dp[0]


def main():
    s = Solution()
    print(s.maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 5979 ms, faster than 81.87% of Python3 online submissions for 
Maximum Score from Performing Multiplication Operations.
Memory Usage: 23.4 MB, less than 97.39% of Python3 online submissions for 
Maximum Score from Performing Multiplication Operations.

2. Runtime: 3318 ms, faster than 99.82% of Python3 online submissions for 
Maximum Score from Performing Multiplication Operations.
Memory Usage: 23.3 MB, less than 97.39% of Python3 online submissions for 
Maximum Score from Performing Multiplication Operations.
"""
