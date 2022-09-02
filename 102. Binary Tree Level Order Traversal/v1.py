from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
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

        ans = [i for i in level_values if i]
        return ans


def main():
    s = Solution()
    print(s.levelOrder(TreeNode(val=3, left=TreeNode(val=9),
                                right=TreeNode(val=20, left=TreeNode(val=15),
                                               right=TreeNode(val=7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 59.74% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15.1 MB, less than 10.09% of Python3 online submissions for Binary Tree Level Order Traversal.

2. Runtime: 59 ms, faster than 39.17% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 15.2 MB, less than 10.09% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
