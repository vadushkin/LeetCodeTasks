from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            temp = head = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = head = ListNode(l2.val)
            l2 = l2.next

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next

        while l1 is not None:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next

        while l2 is not None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next
        return head


"""Tests:
1. Runtime: 68 ms, faster than 29.43% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 79.56% of Python3 online submissions for Merge Two Sorted Lists.

2. Runtime: 56 ms, faster than 57.07% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 79.56% of Python3 online submissions for Merge Two Sorted Lists.
"""