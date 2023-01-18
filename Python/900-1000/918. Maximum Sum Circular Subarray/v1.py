class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0

        for a in nums:
            cur_max = max(cur_max + a, a)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + a, a)
            min_sum = min(min_sum, cur_min)
            total += a

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


def main():
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 550 ms Beats 80.20%
   Memory 19 MB Beats 43.34%

2. Runtime 533 ms Beats 88.35%
   Memory 18.9 MB Beats 73.46%
"""
