from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        d, s = [], []

        for i in lists:
            while i:
                d.append(i.val)
                i = i.next

        for e, i in enumerate(sorted(d, reverse=True)):
            if e == 0:
                s.append(ListNode(i, None))
                continue

            s.append(ListNode(i, s.pop()))

        if s:
            return s[0]

        return None


def main():
    s = Solution()
    print(s.mergeKLists(
        [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 99 ms, faster than 97.68% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.3 MB, less than 28.89% of Python3 online submissions for Merge k Sorted Lists.

2. Runtime: 101 ms, faster than 96.83% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.4 MB, less than 28.89% of Python3 online submissions for Merge k Sorted Lists.
"""
