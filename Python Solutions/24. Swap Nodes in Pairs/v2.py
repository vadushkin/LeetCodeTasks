class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


def main():
    s = Solution()
    # print(s.swapPairs([]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 34 ms, faster than 90.75% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 65.52% of Python3 online submissions for Swap Nodes in Pairs.

2. Runtime: 44 ms, faster than 64.48% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.8 MB, less than 97.71% of Python3 online submissions for Swap Nodes in Pairs.

3. Runtime: 54 ms, faster than 36.51% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.8 MB, less than 97.71% of Python3 online submissions for Swap Nodes in Pairs.
"""
