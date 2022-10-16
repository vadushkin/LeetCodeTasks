from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        elif depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            if root.left:
                self.addOneRow(root.left, val, depth - 1)
            if root.right:
                self.addOneRow(root.right, val, depth - 1)
        return root


def main():
    s = Solution()
    print(s.addOneRow(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1))), val=1, depth=3))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 123 ms, faster than 16.06% of Python3 online submissions for Add One Row to Tree.
Memory Usage: 17.4 MB, less than 37.27% of Python3 online submissions for Add One Row to Tree.

2. Runtime: 66 ms, faster than 80.91% of Python3 online submissions for Add One Row to Tree.
Memory Usage: 17.4 MB, less than 37.27% of Python3 online submissions for Add One Row to Tree.
"""
