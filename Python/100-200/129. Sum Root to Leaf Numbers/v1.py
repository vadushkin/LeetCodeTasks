from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = None

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, path):
        if root:
            if not root.left and not root.right:
                path = path * 10 + root.val
                self.res += path

            self.dfs(root.left, path * 10 + root.val)
            self.dfs(root.right, path * 10 + root.val)


def main():
    s = Solution()
    print(s.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 33 ms Beats 62.11% 
   Memory 13.9 MB Beats 54.57%

2. Runtime 34 ms Beats 55.11% 
   Memory 13.8 MB Beats 54.57%
"""
