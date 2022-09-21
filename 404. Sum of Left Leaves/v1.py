# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)
            else:
                return dfs(node.left) + dfs(node.right)

        return dfs(root)


def main():
    s = Solution()
    print(s.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 46.65% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.8 MB, less than 45.73% of Python3 online submissions for Sum of Left Leaves.

2. Runtime: 63 ms, faster than 28.67% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.7 MB, less than 72.09% of Python3 online submissions for Sum of Left Leaves.
"""
