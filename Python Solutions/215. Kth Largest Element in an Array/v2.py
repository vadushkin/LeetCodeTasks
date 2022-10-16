import heapq


class Solution:
    def findKthLargest(self, nums, k):
        pq = nums[:k]
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x)
            heapq.heappop(pq)
        return pq[0]


s = Solution()
print(s.findKthLargest([1, 2, 3, 4, 5], 1))

"""Tests:
1. Runtime: 776 ms, faster than 30.76% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 28.2 MB, less than 12.68% of Python3 online submissions for Kth Largest Element in an Array.

2. Runtime: 1163 ms, faster than 15.69% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 28.3 MB, less than 12.68% of Python3 online submissions for Kth Largest Element in an Array.
"""