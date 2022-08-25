from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        d, s = [], []
        while head:
            d.append(head.val)
            head = head.next
        if k != len(d):
            for e, i in enumerate(d, start=1):
                if e == 0:
                    continue
                if e % k == 0:
                    d[e - k: e] = reversed(d[e - k: e])
            d = reversed(d)
        for e, i in enumerate(d):
            if e == 0:
                s.append(ListNode(i, None))
                continue
            s.append(ListNode(i, s.pop()))
        if s:
            return s[0]
        return None


def main():
    s = Solution()
    # print(s.reverseKGroup([]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 74 ms, faster than 56.11% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.8 MB, less than 7.55% of Python3 online submissions for Reverse Nodes in k-Group.

2. Runtime: 104 ms, faster than 11.49% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.6 MB, less than 9.44% of Python3 online submissions for Reverse Nodes in k-Group.

3. Runtime: 99 ms, faster than 15.85% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 15.9 MB, less than 7.55% of Python3 online submissions for Reverse Nodes in k-Group.
"""
