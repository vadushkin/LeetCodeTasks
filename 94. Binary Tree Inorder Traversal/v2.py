class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


def main():
    s = Solution()
    print(s.inorderTraversal(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 64 ms, faster than 10.34% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 96.73% of Python3 online submissions for Binary Tree Inorder Traversal.

2. Runtime: 70 ms, faster than 5.63% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 96.73% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
