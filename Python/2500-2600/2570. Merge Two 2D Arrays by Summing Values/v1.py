class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        res = []

        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)

        while i < l1 and j < l2:
            if nums1[i][0] == nums2[j][0]:
                res.append(nums1[i])
                res[-1][1] = nums1[i][1] + nums2[j][1]
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < l1:
            res.append(nums1[i])
            i += 1

        while j < l2:
            res.append(nums2[j])
            j += 1

        return res


def main():
    s = Solution()
    print(s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 60 ms Beats 87.83% 
   Memory 14.1 MB Beats 80.50%

2. Runtime 66 ms Beats 58.5% 
   Memory 13.9 MB Beats 97.86%
"""
