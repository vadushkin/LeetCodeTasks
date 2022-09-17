from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True


def main():
    s = Solution()
    print(s.isSameTree(TreeNode(3, left=TreeNode(2), right=TreeNode(3)),
                       TreeNode(3, left=TreeNode(2), right=TreeNode(3))
                       ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 80 ms, faster than 5.01% of Python3 online submissions for Same Tree.
Memory Usage: 14 MB, less than 29.09% of Python3 online submissions for Same Tree.

2. Runtime: 59 ms, faster than 23.61% of Python3 online submissions for Same Tree.
Memory Usage: 13.9 MB, less than 29.09% of Python3 online submissions for Same Tree.
"""
