class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
            nums.pop(0)
        return 0 if len(nums) < 3 else sum(nums[:3])


def main():
    s = Solution()
    print(s.largestPerimeter([3, 4, 2]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 210 ms, faster than 87.84% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 8.94% of Python3 online submissions for Largest Perimeter Triangle.

2. Runtime: 538 ms, faster than 7.70% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.4 MB, less than 91.63% of Python3 online submissions for Largest Perimeter Triangle.
"""
