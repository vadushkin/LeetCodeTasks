from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.total

    def dfs(self, node: Optional[TreeNode], low: int, high: int) -> None:
        if node is None:
            return

        if low <= node.val <= high:
            self.total += node.val

        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)


def main():
    s = Solution()
    print(s.rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, right=TreeNode(18))), 7, 15))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 268 ms Beats 81.41%
   Memory 23 MB Beats 92.23%

2. Runtime 938 ms Beats 5.3%
   Memory 23 MB Beats 50.66%
"""
