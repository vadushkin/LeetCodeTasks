from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dictionary = {}
        while head:
            if head in dictionary:
                return True
            else:
                dictionary[head] = True
            head = head.next
        return False


def main():
    s = Solution()
    # print(s.hasCycle())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 135 ms, faster than 10.47% of Python3 online submissions for Linked List Cycle.
Memory Usage: 18 MB, less than 10.33% of Python3 online submissions for Linked List Cycle.

2. Runtime: 132 ms, faster than 12.33% of Python3 online submissions for Linked List Cycle.
Memory Usage: 18 MB, less than 10.33% of Python3 online submissions for Linked List Cycle.
"""
