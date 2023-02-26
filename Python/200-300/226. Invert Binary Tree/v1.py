# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left)) if root else None


def main():
    s = Solution()
    print(s.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 31 ms Beats 76.17% 
   Memory 13.8 MB Beats 47.43%

2. Runtime 36 ms Beats 41.91% 
   Memory 13.8 MB Beats 95.8%
"""
