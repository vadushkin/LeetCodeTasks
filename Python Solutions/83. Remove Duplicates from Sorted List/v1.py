from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head


def main():
    s = Solution()
    print(s.deleteDuplicates(ListNode(val=1, next=ListNode(val=1, next=ListNode(val=1, next=None)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 94 ms, faster than 8.30% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.9 MB, less than 72.40% of Python3 online submissions for Remove Duplicates from Sorted List.

2. Runtime: 87 ms, faster than 15.75% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.9 MB, less than 72.40% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
