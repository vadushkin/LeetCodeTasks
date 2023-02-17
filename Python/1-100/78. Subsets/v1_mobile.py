class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in sorted(nums):

            res += [item + [num] for item in res]

        return res
