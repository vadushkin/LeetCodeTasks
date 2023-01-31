class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        return min(set(nums1) & set(nums2), default=-1)


def main():
    s = Solution()
    print(s.getCommon([1, 2, 3], [2, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 454 ms Beats 93.7%
   Memory 39.6 MB Beats 12.82%

2. Runtime 491 ms Beats 69.50%
   Memory 39.6 MB Beats 25.46%
"""
