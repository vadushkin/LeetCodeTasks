from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        if n == 1:
            return None
        n //= 2
        curr = head
        i = 1
        while i < n:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head


def main():
    s = Solution()
    print(s.deleteMiddle(ListNode(1, ListNode(2))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4291 ms, faster than 19.80% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 60.6 MB, less than 79.89% of Python3 online submissions for Delete the Middle Node of a Linked List.

2. Runtime: 3005 ms, faster than 62.80% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 60.1 MB, less than 94.23% of Python3 online submissions for Delete the Middle Node of a Linked List.
"""
