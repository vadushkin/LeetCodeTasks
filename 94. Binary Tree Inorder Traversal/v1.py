# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []

        def drf(current_node):
            if current_node.left:
                drf(current_node.left)
            result.append(current_node.val)
            if current_node.right:
                drf(current_node.right)

        if root:
            drf(root)
        return result


def main():
    s = Solution()
    print(s.inorderTraversal(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 56 ms, faster than 27.26% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.8 MB, less than 96.73% of Python3 online submissions for Binary Tree Inorder Traversal.

2. Runtime: 60 ms, faster than 17.62% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 60.15% of Python3 online submissions for Binary Tree Inorder Traversal.
"""
