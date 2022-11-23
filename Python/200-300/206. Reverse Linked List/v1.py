from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return new_head


def main():
    s = Solution()
    print(s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 72 ms Beats 44.47%
   Memory 20.5 MB Beats 8.34%

2. Runtime 79 ms Beats 22.39%
   Memory 20.5 MB Beats 8.34%
"""
