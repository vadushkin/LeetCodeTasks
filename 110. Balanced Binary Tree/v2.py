from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode], level=1):
        if not root:
            return level

        left = self.isBalanced(root.left, level + 1)
        if not left:
            return

        right = self.isBalanced(root.right, level + 1)
        if not right:
            return

        return abs(left - right) <= 1 and max(left, right)


def main():
    s = Solution()
    print(s.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 43 ms, faster than 99.42% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.6 MB, less than 90.53% of Python3 online submissions for Balanced Binary Tree.

2. Runtime: 94 ms, faster than 49.58% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 19 MB, less than 11.07% of Python3 online submissions for Balanced Binary Tree.
"""
