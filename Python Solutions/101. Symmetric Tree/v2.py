from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(left_node, right_node):
            if not left_node and not right_node:
                return True
            if left_node and right_node and left_node.val == right_node.val:
                return isSym(left_node.left, right_node.right) and isSym(left_node.right, right_node.left)
            return False

        return isSym(root, root)


def main():
    s = Solution()
    print(s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 66 ms, faster than 23.77% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.8 MB, less than 99.62% of Python3 online submissions for Symmetric Tree.

2. Runtime: 40 ms, faster than 84.57% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.9 MB, less than 60.83% of Python3 online submissions for Symmetric Tree.
"""
