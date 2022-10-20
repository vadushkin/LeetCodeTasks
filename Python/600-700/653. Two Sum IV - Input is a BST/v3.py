from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = {}

        def helper(node):
            if not node:
                return False
            if node.val in vals:
                return True
            vals[k - node.val] = True
            return helper(node.left) or helper(node.right)

        return helper(root)


def main():
    s = Solution()
    print(s.findTarget(TreeNode(5, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(7, right=TreeNode(6))), 9))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 183 ms, faster than 32.18% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 18.1 MB, less than 59.20% of Python3 online submissions for Two Sum IV - Input is a BST.

2. Runtime: 162 ms, faster than 47.55% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 18.3 MB, less than 40.47% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
