from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        return self._findTarget(root, set(), k)

    def _findTarget(self, node: Optional[TreeNode], nodes: set, k: int) -> bool:
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True

        nodes.add(node.val)

        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)


def main():
    s = Solution()
    print(s.findTarget(TreeNode(5, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(7, right=TreeNode(6))), 9))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 200 ms, faster than 22.55% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 18.1 MB, less than 59.20% of Python3 online submissions for Two Sum IV - Input is a BST.

2. Runtime: 147 ms, faster than 58.39% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 18.2 MB, less than 47.91% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
