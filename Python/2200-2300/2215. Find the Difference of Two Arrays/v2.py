class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        d = {}

        for i in nums1:
            if i not in d.keys():
                d[i] = 1

        for i in nums2:
            if i in d.keys():
                d[i] = 2

        l1 = []
        l2 = []

        for i in set(nums1):
            if d[i] != 2:
                l1.append(i)

        for i in set(nums2):
            if i not in d.keys():
                l2.append(i)

        return [l1, l2]


def main():
    s = Solution()
    print(s.findDifference([1, 2, 3], [2, 4, 5]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 196 ms Beats 81.3%
   Memory 14.4 MB Beats 52.73%

2. Runtime 194 ms Beats 82.8%
   Memory 14.3 MB Beats 52.73%
"""
