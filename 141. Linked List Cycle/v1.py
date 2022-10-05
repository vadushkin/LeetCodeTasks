from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


def main():
    s = Solution()
    # print(s.hasCycle())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 110 ms, faster than 36.64% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.6 MB, less than 66.81% of Python3 online submissions for Linked List Cycle.

2. Runtime: 63 ms, faster than 86.59% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.5 MB, less than 94.41% of Python3 online submissions for Linked List Cycle.
"""
