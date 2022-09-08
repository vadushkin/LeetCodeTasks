# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []


def main():
    s = Solution()
    print(s.preorderTraversal(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 34 ms, faster than 89.19% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.8 MB, less than 60.30% of Python3 online submissions for Binary Tree Preorder Traversal.

2. Runtime: 63 ms, faster than 11.98% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 60.30% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
