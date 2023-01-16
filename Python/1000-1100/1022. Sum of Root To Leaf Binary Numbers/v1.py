from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], val=0) -> int:
        if not root:
            return 0

        val = val * 2 + root.val

        if root.left == root.right:
            return val

        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)


def main():
    s = Solution()
    print(s.sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 32 ms Beats 97.20%
   Memory 14.2 MB Beats 37.85%

2. Runtime 32 ms Beats 97.20% 
   Memory 14.2 MB Beats 78.27%
"""
