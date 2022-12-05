from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        return slow


def main():
    s = Solution()
    print(s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 70 ms Beats 7.42%
   Memory 13.8 MB Beats 55.96%

2. Runtime 57 ms Beats 47.78%
   Memory 13.9 MB Beats 11.63%
"""
