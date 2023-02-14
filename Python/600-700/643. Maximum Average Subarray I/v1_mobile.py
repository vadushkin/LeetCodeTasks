class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        maxSums = sums
        for i in range(len(nums)-k):
            sums -= nums[i]
            sums += nums[i+k]
            maxSums = max(maxSums, sums)
        return maxSums/k
