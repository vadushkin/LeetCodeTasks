class Solution:
    def mergeTwoLists(self, list1, list2):
        return sorted(list1 + list2)


s = Solution()
print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))

"""Tests:
1. Quickly.
 
2. Quickly.
"""
