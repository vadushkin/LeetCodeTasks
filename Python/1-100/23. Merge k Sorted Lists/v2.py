from heapq import heappush, heappop
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap, res = [], ListNode()

        for index, list_node in enumerate(lists):
            if list_node:
                heappush(heap, (list_node.val, index, list_node))

        curr = res

        while heap:
            _, index, list_node = heappop(heap)

            if list_node.next:
                heappush(heap, (list_node.next.val, index, list_node.next))

            curr.next, curr = list_node, list_node

        return res.next


def main():
    s = Solution()
    print(s.mergeKLists(
        [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 129 ms, faster than 79.69% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.9 MB, less than 45.65% of Python3 online submissions for Merge k Sorted Lists.

2. Runtime: 145 ms, faster than 70.33% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.8 MB, less than 52.43% of Python3 online submissions for Merge k Sorted Lists.
"""
