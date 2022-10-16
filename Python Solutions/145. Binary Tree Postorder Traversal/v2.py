class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return traversal[::-1]


def main():
    s = Solution()
    print(s.postorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 50 ms, faster than 44.95% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.9 MB, less than 13.71% of Python3 online submissions for Binary Tree Postorder Traversal.

2. Runtime: 62 ms, faster than 13.69% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.8 MB, less than 96.72% of Python3 online submissions for Binary Tree Postorder Traversal.
"""
