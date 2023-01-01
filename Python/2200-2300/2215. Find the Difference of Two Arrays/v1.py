class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]


def main():
    s = Solution()
    print(s.findDifference([1, 2, 3], [2, 4, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 192 ms Beats 83.57%
   Memory 14.3 MB Beats 83.20%

2. Runtime 165 ms Beats 100%
   Memory 14.3 MB Beats 52.73%
"""
