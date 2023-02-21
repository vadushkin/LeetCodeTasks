from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        temp.next = list1 or list2

        return dummy.next


def main():
    s = Solution()
    print(s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(3))), ListNode(2, ListNode(3, ListNode(5)))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 34 ms Beats 89.26% 
   Memory 13.8 MB Beats 98.61%

2. Runtime 41 ms Beats 52.97% 
   Memory 13.8 MB Beats 98.61%
"""
