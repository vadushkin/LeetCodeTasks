from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
        current = root

        while current:
            if current.val < p.val and current.val < q.val:
                current = current.right
            elif current.val > p.val and current.val > q.val:
                current = current.left
            else:
                return current


def main():
    s = Solution()
    print(s.lowestCommonAncestor(TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(1), TreeNode(3)))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 77 ms Beats 83.97% 
   Memory 18.6 MB Beats 96.78%

2. Runtime 76 ms Beats 87.3% 
   Memory 18.7 MB Beats 96.78%
"""
