class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev, cur, res = 0, 0, 0

        for n in nums:

            cur = cur + 1 if prev < n else 1

            res = max(res, cur)

            prev = n

        return res
