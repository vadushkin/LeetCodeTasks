# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans_r, ans_l = [], []

        def dfs_left(node):
            if not node:
                ans_l.append(None)
                return
            ans_l.append(node.val)
            dfs_left(node.left)
            dfs_left(node.right)

        def dfs_right(node):
            if not node:
                ans_r.append(None)
                return
            ans_r.append(node.val)
            dfs_right(node.right)
            dfs_right(node.left)

        dfs_left(root.left)
        dfs_right(root.right)

        return ans_r == ans_l


def main():
    s = Solution()
    print(s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(3)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 73 ms, faster than 11.20% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14 MB, less than 21.79% of Python3 online submissions for Symmetric Tree.

2. Runtime: 44 ms, faster than 75.70% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.1 MB, less than 21.79% of Python3 online submissions for Symmetric Tree.
"""
