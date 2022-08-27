from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 73 ms, faster than 91.47% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.9 MB, less than 38.79% of Python3 online submissions for Remove Linked List Elements.

2. Runtime: 145 ms, faster than 8.87% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.9 MB, less than 38.79% of Python3 online submissions for Remove Linked List Elements.
"""
