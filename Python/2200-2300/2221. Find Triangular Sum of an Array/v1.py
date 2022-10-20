class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 0:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1
        return nums[0]


def main():
    s = Solution()
    print(s.triangularSum([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4015 ms, faster than 52.39% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 14 MB, less than 50.26% of Python3 online submissions for Find Triangular Sum of an Array.

2. Runtime: 2289 ms, faster than 86.09% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 14 MB, less than 50.26% of Python3 online submissions for Find Triangular Sum of an Array.
"""
