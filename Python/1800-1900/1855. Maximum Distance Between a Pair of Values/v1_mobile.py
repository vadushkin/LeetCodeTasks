class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res, j = 0, -1

        for i, a in enumerate(nums1):

            while j + 1 < len(nums2) and a <= nums2[j + 1]:

                j += 1

            res = max(res, j - i)

        return res
