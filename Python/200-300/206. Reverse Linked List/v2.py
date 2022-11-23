from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


def main():
    s = Solution()
    print(s.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 41 ms Beats 88.4%
   Memory 15.4 MB Beats 55.78%

2. Runtime 41 ms Beats 88.4%
   Memory 15.4 MB Beats 55.78%
"""
