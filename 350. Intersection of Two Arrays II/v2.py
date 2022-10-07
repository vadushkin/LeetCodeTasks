from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return (Counter(nums1) & Counter(nums2)).elements()


def main():
    s = Solution()
    print(s.intersect([1, 2, 3, 4], [2, 3]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 87 ms, faster than 56.20% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.9 MB, less than 84.53% of Python3 online submissions for Intersection of Two Arrays II.

2. Runtime: 87 ms, faster than 56.20% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 15.01% of Python3 online submissions for Intersection of Two Arrays II.
"""
