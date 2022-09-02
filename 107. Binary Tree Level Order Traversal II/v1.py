# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        level_count = defaultdict(int)
        level_values = []

        def dfs(node=root, level=0):
            if not node:
                return
            level_values.append([])
            level_count[level] += 1
            level_values[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs()

        ans = [i for i in level_values[::-1] if i]
        return ans


def main():
    s = Solution()
    print(s.levelOrderBottom(TreeNode(val=3, left=TreeNode(val=9),
                                      right=TreeNode(val=20, left=TreeNode(val=15),
                                                     right=TreeNode(val=7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 48 ms, faster than 66.63% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 15.2 MB, less than 7.67% of Python3 online submissions for Binary Tree Level Order Traversal II.

2. Runtime: 76 ms, faster than 7.48% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 15.3 MB, less than 7.67% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
