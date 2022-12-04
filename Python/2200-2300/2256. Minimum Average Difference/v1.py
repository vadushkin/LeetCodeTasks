class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = -1
        min_avg_diff = float("inf")

        for index in range(n):
            left_part_average = 0

            for i in range(index + 1):
                left_part_average += nums[i]

            left_part_average //= (index + 1)
            right_part_average = 0

            for j in range(index + 1, n):
                right_part_average += nums[j]

            if index != n - 1:
                right_part_average //= (n - index - 1)

            curr_difference = abs(left_part_average - right_part_average)

            if curr_difference < min_avg_diff:
                min_avg_diff = curr_difference
                ans = index

        return ans


def main():
    s = Solution()
    print(s.minimumAverageDifference([2, 5, 3, 9, 5, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Time Limit Exceeded 
   60 / 78 testcases passed

2. Time Limit Exceeded
   60 / 78 testcases passed
"""
