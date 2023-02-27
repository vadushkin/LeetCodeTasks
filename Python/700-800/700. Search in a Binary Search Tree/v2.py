# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchBST(root.left, val) if root and val < root.val else self.searchBST(
            root.right, val) if root and val > root.val else root


def main():
    s = Solution()
    print(s.searchBST(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5)), 2))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 67 ms Beats 98.14% 
   Memory 16.5 MB Beats 16.45%

2. Runtime 84 ms Beats 40.83% 
   Memory 16.5 MB Beats 62.18%
"""
