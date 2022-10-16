class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        L, _ = len(nums), nums.sort()
        for i in range(L - 1, 1, -1):
            a = nums[i]
            for j in range(i - 1, 0, -1):
                b, m, c = nums[j], a - nums[j] + 1, nums[j - 1]
                if m > b:
                    break
                if c >= m:
                    return a + b + c
        return 0


def main():
    s = Solution()
    print(s.largestPerimeter([1, 2, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 505 ms, faster than 13.51% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.2 MB, less than 99.79% of Python3 online submissions for Largest Perimeter Triangle.

2. Runtime: 274 ms, faster than 73.40% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
"""
