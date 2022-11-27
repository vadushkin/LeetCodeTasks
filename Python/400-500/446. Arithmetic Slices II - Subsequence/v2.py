import collections


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        sum_len = 0
        N = len(nums)

        if N <= 2:
            return 0

        diff_array = [collections.defaultdict(int) for _ in range(N)]
        dp = [collections.defaultdict(int) for _ in range(N)]

        for i in range(1, N):
            for j in range(i):
                diff_array[i][nums[i] - nums[j]] += 1

        dp[0] = dp[1] = {}

        for i in range(2, N):
            for j in range(i):
                diff = nums[i] - nums[j]

                if diff in diff_array[j]:
                    dp[i][diff] += diff_array[j][diff]
                    sum_len += diff_array[j][diff]

                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    sum_len += dp[j][diff]

        return sum_len


def main():
    s = Solution()
    print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 1700 ms Beats 65.9%
   Memory 52.4 MB Beats 68.64%

2. Runtime 1276 ms Beats 82.84%
   Memory 52.5 MB Beats 68.64%
"""
