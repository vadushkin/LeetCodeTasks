from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        slower, faster = head, head.next.next

        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next

        slower.next = slower.next.next

        return head


def main():
    s = Solution()
    print(s.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 4362 ms, faster than 16.68% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 60.5 MB, less than 79.89% of Python3 online submissions for Delete the Middle Node of a Linked List.

2. Runtime: 4057 ms, faster than 31.47% of Python3 online submissions for Delete the Middle Node of a Linked List.
Memory Usage: 60.6 MB, less than 79.89% of Python3 online submissions for Delete the Middle Node of a Linked List.
"""
