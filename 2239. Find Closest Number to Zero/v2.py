class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        pos = 999999
        neg = -pos
        for x in nums:
            if neg < x < pos:
                if x < 0:
                    neg = x
                else:
                    pos = x
        return pos if pos <= -neg else neg


def main():
    s = Solution()
    print(s.findClosestNumber([-1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 190 ms, faster than 78.22% of Python3 online submissions for Find Closest Number to Zero.
Memory Usage: 14.1 MB, less than 48.20% of Python3 online submissions for Find Closest Number to Zero.

2. Runtime: 389 ms, faster than 11.83% of Python3 online submissions for Find Closest Number to Zero.
Memory Usage: 14.2 MB, less than 48.20% of Python3 online submissions for Find Closest Number to Zero.
"""
