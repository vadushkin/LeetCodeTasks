class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)),
                   self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))
                   ) if root else mx - mn


def main():
    s = Solution()
    print(s.maxAncestorDiff(TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
                                     TreeNode(10, right=TreeNode(14, right=TreeNode(13))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 72 ms Beats 61.16%
   Memory 20.1 MB Beats 32.9%

2. Runtime 70 ms Beats 63.24%
   Memory 19.9 MB Beats 60.12%
"""
