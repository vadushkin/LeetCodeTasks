from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1


def main():
    s = Solution()
    print(s.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 104 ms, faster than 36.72% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.6 MB, less than 60.80% of Python3 online submissions for Balanced Binary Tree.

2. Runtime: 43 ms, faster than 99.42% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.6 MB, less than 90.53% of Python3 online submissions for Balanced Binary Tree.
"""
