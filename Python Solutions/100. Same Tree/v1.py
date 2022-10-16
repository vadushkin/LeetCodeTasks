# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list_p = self.dfs(p, [])
        list_q = self.dfs(q, [])
        return list_p == list_q

    def dfs(self, node, list_values):
        if not node:
            list_values.append(None)
            return
        list_values.append(node.val)
        self.dfs(node.left, list_values)
        self.dfs(node.right, list_values)
        return list_values


def main():
    s = Solution()
    print(s.isSameTree(TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
                       TreeNode(1, left=TreeNode(2), right=TreeNode(3))
                       ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 63 ms, faster than 14.78% of Python3 online submissions for Same Tree.
Memory Usage: 13.9 MB, less than 75.68% of Python3 online submissions for Same Tree.
    
2. Runtime: 30 ms, faster than 95.65% of Python3 online submissions for Same Tree.
Memory Usage: 13.8 MB, less than 75.68% of Python3 online submissions for Same Tree.
"""
