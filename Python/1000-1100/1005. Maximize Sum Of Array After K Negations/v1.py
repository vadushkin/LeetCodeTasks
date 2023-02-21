class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = 0

        while i < len(nums) and i < k and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1

        return sum(nums) - (k - i) % 2 * min(nums) * 2


def main():
    s = Solution()
    print(s.largestSumAfterKNegations([4, 2, 3], 1))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 47 ms Beats 87.87% 
   Memory 14 MB Beats 46.71%

2. Runtime 47 ms Beats 87.87% 
   Memory 14 MB Beats 46.71%
"""
