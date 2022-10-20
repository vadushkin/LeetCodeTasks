class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        d, s = [], []
        while head:
            d.append(head.val)
            head = head.next
        for e, i in enumerate(d):
            if e % 2 != 0:
                d[e], d[e - 1] = d[e - 1], d[e]
        for e, i in enumerate(reversed(d)):
            if e == 0:
                s.append(ListNode(i, None))
                continue
            s.append(ListNode(i, s.pop()))
        if s:
            return s[0]
        return None


def main():
    s = Solution()
    # print(s.swapPairs([]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 41 ms, faster than 72.70% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 65.52% of Python3 online submissions for Swap Nodes in Pairs.

2. Runtime: 33 ms, faster than 92.33% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 14 MB, less than 19.29% of Python3 online submissions for Swap Nodes in Pairs.

3. Runtime: 53 ms, faster than 39.21% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.6 MB, less than 99.93% of Python3 online submissions for Swap Nodes in Pairs.
"""
