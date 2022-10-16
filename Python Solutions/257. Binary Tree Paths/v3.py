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
        if not root.left and not root.right:
            return [str(root.val)]
        tree_paths = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        tree_paths += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return tree_paths


def main():
    s = Solution()
    print(s.binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5, TreeNode(10)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 72 ms, faster than 10.97% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.8 MB, less than 75.09% of Python3 online submissions for Binary Tree Paths.

2. Runtime: 41 ms, faster than 81.01% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.8 MB, less than 98.08% of Python3 online submissions for Binary Tree Paths.
"""
