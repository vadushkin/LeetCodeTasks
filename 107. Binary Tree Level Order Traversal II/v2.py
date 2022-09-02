# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        queue, nodes = [root], []
        while queue:
            nodes.append([q.val for q in queue])
            queue = [q for node in queue for q in (node.left, node.right) if q]
        nodes.reverse()
        return nodes


def main():
    s = Solution()
    print(s.levelOrderBottom(TreeNode(val=3, left=TreeNode(val=9),
                                      right=TreeNode(val=20, left=TreeNode(val=15),
                                                     right=TreeNode(val=7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 46.88% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.2 MB, less than 49.26% of Python3 online submissions for Binary Tree Level Order Traversal II.

2. Runtime: 44 ms, faster than 76.42% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.3 MB, less than 49.26% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
