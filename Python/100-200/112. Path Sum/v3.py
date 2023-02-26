# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        return root and (
            root.val == target_sum and not root.left and not root.right or self.hasPathSum(
                root.left, target_sum - root.val) or self.hasPathSum(root.right, target_sum - root.val)
        )


def main():
    s = Solution()
    print(s.hasPathSum(
        TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=9, left=TreeNode(val=7), right=TreeNode(val=2))),
                 right=TreeNode(val=8, left=TreeNode(val=13),
                                right=TreeNode(val=4, left=TreeNode(val=5), right=TreeNode(val=1)))), 20))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 44 ms Beats 70.69% 
   Memory 15 MB Beats 47.94%

2. Runtime 49 ms Beats 40.88% 
   Memory 15 MB Beats 88.82%
"""
