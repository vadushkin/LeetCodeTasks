from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        return root if (root.val - p.val) * (root.val - q.val) < 1 else \
            self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)


def main():
    s = Solution()
    print(s.lowestCommonAncestor(TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(1), TreeNode(3)))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 77 ms Beats 83.97% 
   Memory 18.6 MB Beats 99.79%

2. Runtime 64 ms Beats 99.58% 
   Memory 18.8 MB Beats 59.93%
"""
