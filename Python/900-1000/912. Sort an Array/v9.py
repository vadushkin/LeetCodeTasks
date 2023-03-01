import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)

        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]

        return self.sortArray(lt) + eq + self.sortArray(gt)


def main():
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 1602 ms Beats 75.9% 
   Memory 23.4 MB Beats 24.60%

2. Runtime 1585 ms Beats 75.71% 
   Memory 23.8 MB Beats 18.65%
"""
