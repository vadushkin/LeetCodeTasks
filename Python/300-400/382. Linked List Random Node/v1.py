import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = []

        while head:
            self.head.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.head)


def main():
    s = Solution(ListNode(1, ListNode(2, ListNode(3))))
    print(s.getRandom())


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 132 ms Beats 22.86% 
   Memory 17.6 MB Beats 15.80%

2. Runtime 100 ms Beats 26.95% 
   Memory 17.4 MB Beats 35.13%
"""
