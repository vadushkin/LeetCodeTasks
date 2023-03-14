from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node:
                return 0

            cur = cur * 10 + node.val

            if not node.left and not node.right:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)


def main():
    s = Solution()
    print(s.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 36 ms Beats 42.8% 
   Memory 13.8 MB Beats 54.57%

2. Runtime 28 ms Beats 88.93% 
   Memory 13.9 MB Beats 10.80%
"""
