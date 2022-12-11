from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> float | int:
        self.get_sum(root)
        return self.max_sum

    def get_sum(self, node: Optional[TreeNode]):
        if not node:
            return 0

        ls, rs = self.get_sum(node.left), self.get_sum(node.right)
        max_single_path = max(node.val + max(ls, rs), node.val)
        self.max_sum = max(self.max_sum, max_single_path, node.val + ls + rs)
        return max_single_path


def main():
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 229 ms Beats 17.50%
   Memory 21.4 MB Beats 31.96%
   
2. Runtime 227 ms Beats 19.14%
   Memory 21.3 MB Beats 63.68%
"""
