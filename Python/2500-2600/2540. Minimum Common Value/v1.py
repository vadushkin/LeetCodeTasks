class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i, len2 = 0, len(nums2)

        for n1 in nums1:
            while i < len2 and nums2[i] < n1:
                i += 1

            if i < len2 and n1 == nums2[i]:
                return n1

        return -1


def main():
    s = Solution()
    print(s.getCommon([1, 2, 3], [2, 4]))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 469 ms Beats 82.64% 
   Memory 32.3 MB Beats 77.90%

2. Runtime 453 ms Beats 93.71%
   Memory 32.2 MB Beats 95.57%
"""
