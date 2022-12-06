from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        t1 = head
        temp = t2 = head.next

        while t2.next and t2.next.next:
            t1.next = t2.next
            t2.next = t2.next.next
            t1 = t1.next
            t2 = t2.next

        if t2.next:
            t1.next = t2.next
            t2.next = None
            t1 = t1.next

        t1.next = temp

        return head


def main():
    s = Solution()
    print(s.oddEvenList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 40 ms Beats 97.67%
   Memory 16.6 MB Beats 78.70%

2. Runtime 53 ms Beats 81.64%
   Memory 16.5 MB Beats 98.80%
"""
