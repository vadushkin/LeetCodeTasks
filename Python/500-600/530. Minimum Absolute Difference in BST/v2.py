from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        output = []
        self.inorder(root, output)

        mini_diff = float('inf')

        for i in range(1, len(output)):
            mini_diff = min(mini_diff, output[i] - output[i - 1])

        return mini_diff

    def inorder(self, root, output):
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)


def main():
    s = Solution()
    print(s.getMinimumDifference(TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, TreeNode(4)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 131 ms, faster than 17.66% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 15.9 MB, less than 80.91% of Python3 online submissions for Minimum Absolute Difference in BST.

2. Runtime: 126 ms, faster than 23.98% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16.1 MB, less than 35.08% of Python3 online submissions for Minimum Absolute Difference in BST.
"""
