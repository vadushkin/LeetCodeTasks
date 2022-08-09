from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        count = 1
        for item in range(1, len(nums)):
            if nums[item] != nums[item - 1]:
                nums[count] = nums[item]
                count += 1

        return count


s = Solution()
print(s.removeDuplicates([1, 2, 34, 1, 1, 2, 3]))


"""Tests:
1. Runtime: 81 ms, faster than 99.17% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 16.41% of Python3 online submissions for Remove Duplicates from Sorted Array.

2. Runtime: 211 ms, faster than 16.51% of Python3 online submissions for Remove Duplicates from Sorted Array. O_O
Memory Usage: 15.6 MB, less than 16.41% of Python3 online submissions for Remove Duplicates from Sorted Array.

3. Runtime: 106 ms, faster than 81.92% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 16.41% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""