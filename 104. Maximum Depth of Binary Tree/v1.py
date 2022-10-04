from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels = []

        def dfs(node: TreeNode, level=0):
            if node is None:
                return

            level += 1
            levels.append(level)

            dfs(node.left, level)
            dfs(node.right, level)

        dfs(root)
        return max(levels) if levels else 0


def main():
    s = Solution()
    print(s.maxDepth(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 70 ms, faster than 55.78% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.5 MB, less than 23.56% of Python3 online submissions for Maximum Depth of Binary Tree.

2. Runtime: 86 ms, faster than 26.07% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.5 MB, less than 23.56% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
