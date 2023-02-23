class Solution:
    def __init__(self):
        self.nums = None

    def rob(self, nums: list[int]) -> int:
        if self.nums is None:
            self.nums = nums

        if len(nums) < 2:
            return max(nums + [0])

        return max(self.helper(1, len(self.nums)), self.helper(0, len(self.nums) - 1))

    def helper(self, left, right):
        last, now = 0, 0

        while left < right:
            last, now, left = now, max(last + self.nums[left], now), left + 1

        return now


def main():
    s = Solution()
    print(s.rob([2, 3, 2]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 41 ms Beats 22.93% 
   Memory 13.8 MB Beats 97.70%

2. Runtime 32 ms Beats 76.7% 
   Memory 13.9 MB Beats 62.36%
"""
