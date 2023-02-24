from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)

        return res


def main():
    s = Solution()
    print(s.postorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 35 ms Beats 46.79% 
   Memory 13.8 MB Beats 50.46%

2. Runtime 38 ms Beats 26.5% 
   Memory 13.9 MB Beats 50.46%
"""
