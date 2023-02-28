class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root, min_value=float("-inf"), max_value=float("inf")) -> bool:
        return root is None or ((min_value < root.val < max_value) and self.isValidBST(root.left, min_value,
                                                                                       root.val) and self.isValidBST(
            root.right, root.val, max_value))


def main():
    s = Solution()
    print(s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 54 ms Beats 28.25% 
   Memory 16.5 MB Beats 72.72%

2. Runtime 42 ms Beats 87.26% 
   Memory 16.4 MB Beats 92.32%
"""
