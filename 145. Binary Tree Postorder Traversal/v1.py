# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []


def main():
    s = Solution()
    print(s.postorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 33 ms, faster than 91.18% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.8 MB, less than 96.72% of Python3 online submissions for Binary Tree Postorder Traversal.

2. Runtime: 63 ms, faster than 11.92% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.9 MB, less than 60.77% of Python3 online submissions for Binary Tree Postorder Traversal.
"""
