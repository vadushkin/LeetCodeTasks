class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result


def main():
    s = Solution()
    print(s.preorderTraversal(TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 64 ms, faster than 10.36% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 13.33% of Python3 online submissions for Binary Tree Preorder Traversal.

2. Runtime: 60 ms, faster than 17.62% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 60.30% of Python3 online submissions for Binary Tree Preorder Traversal.
"""
