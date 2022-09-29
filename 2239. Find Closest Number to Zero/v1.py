class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        return max([-abs(a), a] for a in nums)[1]


def main():
    s = Solution()
    print(s.findClosestNumber([-4, -2, -1, 0, 1, 4, 8]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 335 ms, faster than 26.99% of Python3 online submissions for Find Closest Number to Zero.
Memory Usage: 14.2 MB, less than 48.20% of Python3 online submissions for Find Closest Number to Zero.

2. Runtime: 372 ms, faster than 15.91% of Python3 online submissions for Find Closest Number to Zero.
Memory Usage: 14 MB, less than 91.00% of Python3 online submissions for Find Closest Number to Zero.
"""
