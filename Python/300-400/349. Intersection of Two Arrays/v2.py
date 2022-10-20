class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


def main():
    s = Solution()
    print(s.intersection([1, 2, 3], [3, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 87 ms, faster than 39.16% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.2 MB, less than 25.09% of Python3 online submissions for Intersection of Two Arrays.

2. Runtime: 101 ms, faster than 22.17% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14 MB, less than 68.57% of Python3 online submissions for Intersection of Two Arrays.
"""
