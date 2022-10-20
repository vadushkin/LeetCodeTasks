class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n, ans, x = len(nums), 0, 1
        for i in range(n):
            ans += (nums[i] * x) % 10
            x = ((n - i - 1) * x) // (i + 1)
        return ans % 10


def main():
    s = Solution()
    print(s.triangularSum([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 285 ms, faster than 90.43% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 13.9 MB, less than 79.07% of Python3 online submissions for Find Triangular Sum of an Array.

2. Runtime: 279 ms, faster than 90.72% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 13.9 MB, less than 79.07% of Python3 online submissions for Find Triangular Sum of an Array.
"""
