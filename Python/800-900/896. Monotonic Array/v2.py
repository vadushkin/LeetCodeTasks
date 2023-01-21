class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
                all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


def main():
    s = Solution()
    print(s.isMonotonic([1, 2, 3, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 988 ms Beats 88.52%
   Memory 28.1 MB Beats 39.71%

2. Runtime 942 ms Beats 98.22% 
   Memory 28 MB Beats 61.12%
"""
