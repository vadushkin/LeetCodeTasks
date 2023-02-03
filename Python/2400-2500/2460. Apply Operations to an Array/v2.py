class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1], nums[i] = nums[i - 1] * 2, 0

        return sorted(nums, key=lambda x: not x)


def main():
    s = Solution()
    print(s.applyOperations([1, 2, 2, 1, 1, 0]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 49 ms Beats 90.89% 
   Memory 14.1 MB Beats 54.21%

2. Runtime 48 ms Beats 93.11% 
   Memory 14.2 MB Beats 54.21%
"""
