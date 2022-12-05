from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def main():
    s = Solution()
    print(s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 55 ms Beats 54.38%
   Memory 14 MB Beats 11.63%

2. Runtime 54 ms Beats 57.39%
   Memory 13.8 MB Beats 55.96%
"""
