class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mirror(self, a, b):
        if not a or not b:
            return not a and not b

        return a.val == b.val and self.mirror(a.left, b.right) and self.mirror(a.right, b.left)

    def isSymmetric(self, root):
        return True if not root else self.mirror(root.left, root.right)


def main():
    s = Solution()
    print(s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 29 ms Beats 93.78% 
   Memory 13.8 MB Beats 91.25%

2. Runtime 33 ms Beats 81.20% 
   Memory 13.9 MB Beats 53.36%
"""
