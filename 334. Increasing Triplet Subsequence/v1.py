import math


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


def main():
    s = Solution()
    print(s.increasingTriplet([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 589 ms, faster than 92.90% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 24.6 MB, less than 80.42% of Python3 online submissions for Increasing Triplet Subsequence.

2. Runtime: 1256 ms, faster than 41.95% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 24.6 MB, less than 48.78% of Python3 online submissions for Increasing Triplet Subsequence.
"""
