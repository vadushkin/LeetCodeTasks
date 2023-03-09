from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        lookup = set()

        while start:
            if start in lookup:
                return start
            else:
                lookup.add(start)
                start = start.next
        return None


def main():
    s = Solution()
    print(s.detectCycle(ListNode(3, ListNode(2, ListNode(0, ListNode(4))))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 55 ms Beats 52.57% 
   Memory 17.9 MB Beats 21.35%

2. Runtime 53 ms Beats 63.17% 
   Memory 18 MB Beats 8.78%
"""
