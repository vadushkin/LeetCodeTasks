from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]


def main():
    s = Solution()
    print(s.binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5, TreeNode(10)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 77 ms, faster than 5.92% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.7 MB, less than 98.08% of Python3 online submissions for Binary Tree Paths.

2. Runtime: 59 ms, faster than 44.20% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.9 MB, less than 75.09% of Python3 online submissions for Binary Tree Paths.
"""
