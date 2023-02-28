from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], less_than=float('inf'), larger_than=float('-inf')) -> bool:
        if not root:
            return True

        if root.val <= larger_than or root.val >= less_than:
            return False

        return self.isValidBST(root.left, min(less_than, root.val), larger_than) and (
            self.isValidBST(root.right, less_than, max(root.val, larger_than)))


def main():
    s = Solution()
    print(s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 45 ms Beats 75.34% 
   Memory 16.4 MB Beats 72.72%

2. Runtime 40 ms Beats 92.32% 
   Memory 16.5 MB Beats 39.23%
"""
