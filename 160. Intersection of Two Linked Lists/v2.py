class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a


def main():
    s = Solution()
    # print(s.getIntersectionNode())


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 407 ms, faster than 11.74% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.5 MB, less than 94.04% of Python3 online submissions for Intersection of Two Linked Lists.

2. Runtime: 387 ms, faster than 15.81% of Python3 online submissions for Intersection of Two Linked Lists.
Memory Usage: 29.5 MB, less than 94.04% of Python3 online submissions for Intersection of Two Linked Lists.
"""
