import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.minimum = 0
        self.maximum = 0
        self.head = head

        tmp = head

        while tmp:
            self.maximum += 1
            tmp = tmp.next

    def getRandom(self) -> int:
        tmp = self.head

        for i in range(random.randint(self.minimum, self.maximum - 1)):
            tmp = tmp.next

        return tmp.val



def main():
    s = Solution(ListNode(1, ListNode(2, ListNode(3))))
    print(s.getRandom())


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 170 ms Beats 18.40% 
   Memory 17.3 MB Beats 73.23%

2. Runtime 135 ms Beats 22.49% 
   Memory 17.3 MB Beats 73.23%
"""
