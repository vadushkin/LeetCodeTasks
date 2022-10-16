from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return head


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 129 ms, faster than 22.75% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.9 MB, less than 13.24% of Python3 online submissions for Remove Linked List Elements.

2. Runtime: 72 ms, faster than 92.78% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.7 MB, less than 82.53% of Python3 online submissions for Remove Linked List Elements.
"""
