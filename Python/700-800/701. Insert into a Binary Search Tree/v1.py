from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root


def main():
    s = Solution()
    print(s.insertIntoBST(TreeNode(4, TreeNode(2, TreeNode(1)), TreeNode(6, TreeNode(7))), 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 135 ms Beats 77.63% 
   Memory 17 MB Beats 43.38%

2. Runtime 136 ms Beats 73.71% 
   Memory 16.9 MB Beats 89.83%
"""
