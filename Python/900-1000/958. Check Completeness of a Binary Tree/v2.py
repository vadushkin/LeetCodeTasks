from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            if left & (left + 1) == 0 and left / 2 <= right <= left:
                return left + right + 1
            if right & (right + 1) == 0 and right <= left <= right * 2 + 1:
                return left + right + 1

            return -1

        return dfs(root) > 0


def main():
    s = Solution()
    print(s.isCompleteTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))


if __name__ == '__main__':
    main()

"""Tests: 
1. Runtime 30 ms Beats 94.47% 
   Memory 14 MB Beats 18.83%

2. Runtime 34 ms Beats 80.48% 
   Memory 14 MB Beats 18.83%
"""
