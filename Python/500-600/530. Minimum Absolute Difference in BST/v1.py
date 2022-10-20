from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, lo, hi):
            if not node:
                return hi - lo

            left = dfs(node.left, lo, node.val)
            right = dfs(node.right, node.val, hi)

            return min(left, right)

        return dfs(root, float('-inf'), float('inf'))


def main():
    s = Solution()
    print(s.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, TreeNode(4)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 107 ms, faster than 50.96% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16 MB, less than 49.09% of Python3 online submissions for Minimum Absolute Difference in BST.

2. Runtime: 59 ms, faster than 90.73% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 15.9 MB, less than 80.91% of Python3 online submissions for Minimum Absolute Difference in BST.
"""
