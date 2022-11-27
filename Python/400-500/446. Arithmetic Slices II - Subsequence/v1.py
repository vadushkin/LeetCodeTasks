from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        freq = [defaultdict(int) for _ in range(len(nums))]

        for i, x in enumerate(nums):
            for ii in range(i):
                diff = x - nums[ii]
                ans += freq[ii].get(diff, 0)
                freq[i][diff] += 1 + freq[ii][diff]

        return ans


def main():
    s = Solution()
    print(s.numberOfArithmeticSlices([2, 4, 6, 8, 10]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 2322 ms Beats 47.93%
   Memory 68.8 MB Beats 55.3%

2. Runtime 1475 ms Beats 75.74%
   Memory 69 MB Beats 38.46%
"""
