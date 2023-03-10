import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = 1

        head = self.head
        ans = self.head

        while head.next:
            n += 1
            head = head.next

            if random.randint(1, n) == (n-1):
                ans = head

        return ans.val

def main():
    s = Solution(ListNode(1, ListNode(2, ListNode(3))))
    print(s.getRandom())


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 340 ms Beats 5.2% 
   Memory 17.6 MB Beats 15.80%

2. Runtime 468 ms Beats 5.2% 
   Memory 17.6 MB Beats 15.80%
"""
