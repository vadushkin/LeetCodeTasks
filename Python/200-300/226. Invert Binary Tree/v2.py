# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right

        return root


def main():
    s = Solution()
    print(s.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 33 ms Beats 64.43% 
   Memory 13.9 MB Beats 6.93%

2. Runtime 34 ms Beats 58.15% 
   Memory 13.8 MB Beats 95.8%
"""
