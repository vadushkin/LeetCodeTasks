class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, curSubset):

            ans.append(curSubset[::])

            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i - 1]: continue 

                curSubset.append(nums[i])

                backtrack(i + 1, curSubset)

                curSubset.pop()

        nums.sort()

        ans = []

        backtrack(0, [])

        return ans
