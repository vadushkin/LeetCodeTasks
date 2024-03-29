from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        while head:
            head.next, prev, head = prev, head, head.next

        return prev


def main():
    s = Solution()
    print(s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 52 ms Beats 13.17% 
   Memory 15.4 MB Beats 90.52%

2. Runtime 46 ms Beats 22.19% 
   Memory 15.2 MB Beats 99.79%
"""
