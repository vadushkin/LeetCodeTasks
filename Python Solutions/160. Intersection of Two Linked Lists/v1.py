from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA


def main():
    s = Solution()
    # print(s.getIntersectionNode())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 176 ms, faster than 85.21% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.5 MB, less than 94.04% of Python3 online submissions for Intersection of Two Linked Lists.

2. Runtime: 411 ms, faster than 10.90% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.4 MB, less than 94.04% of Python3 online submissions for Intersection of Two Linked Lists.
"""
