from heapq import heappush, heappop


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return


class Solution:
    def mergeKLists(self, lists: list[[ListNode]]) -> [ListNode]:
        heap, res = [], ListNode()
        for i, L in enumerate(lists):
            if L:
                heappush(heap, (L.val, i, L))
        curr = res
        while heap:
            _, i, L = heappop(heap)
            if L.next:
                heappush(heap, (L.next.val, i, L.next))
            curr.next, curr = L, L
        return res.next


def main():
    s = Solution()
    print(s.mergeKLists([[1, 2, 3], [4, 5, 6], [1, 2, 3]]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 129 ms, faster than 79.69% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.9 MB, less than 45.65% of Python3 online submissions for Merge k Sorted Lists.

2. Runtime: 145 ms, faster than 70.33% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.8 MB, less than 52.43% of Python3 online submissions for Merge k Sorted Lists.
"""
