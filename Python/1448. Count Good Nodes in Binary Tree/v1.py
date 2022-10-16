from collections import deque
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        q = deque()
        q.append((root, -inf))
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                ans += 1
            if node.left:
                q.append((node.left, max(max_val, node.val)))
            if node.right:
                q.append((node.right, max(max_val, node.val)))
        return ans


def main():
    s = Solution()
    print(s.goodNodes(TreeNode(val=3, left=TreeNode(val=1, left=TreeNode(val=3)),
                               right=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 505 ms, faster than 15.65% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.5 MB, less than 87.02% of Python3 online submissions for Count Good Nodes in Binary Tree.

2. Runtime: 629 ms, faster than 5.03% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.6 MB, less than 46.30% of Python3 online submissions for Count Good Nodes in Binary Tree.
"""
