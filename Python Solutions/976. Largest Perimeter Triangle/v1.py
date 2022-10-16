class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i + 2] < nums[i + 1] + nums[i]:
                ans = sum(nums[i:i + 3])
        return ans


def main():
    s = Solution()
    print(s.largestPerimeter([2, 5, 4]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 595 ms, faster than 5.00% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.4 MB, less than 91.63% of Python3 online submissions for Largest Perimeter Triangle.

2. Runtime: 248 ms, faster than 80.14% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
"""
