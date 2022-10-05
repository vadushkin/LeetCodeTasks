from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy, dummy.left = TreeNode(), root
        row = [dummy]
        for _ in range(depth - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right
        return dummy.left


def main():
    s = Solution()
    print(s.addOneRow(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1))), val=1, depth=3))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime: 98 ms, faster than 48.94% of Python3 online submissions for Add One Row to Tree.
Memory Usage: 16.7 MB, less than 69.24% of Python3 online submissions for Add One Row to Tree.

2. Runtime: 115 ms, faster than 25.45% of Python3 online submissions for Add One Row to Tree.
Memory Usage: 16.7 MB, less than 69.24% of Python3 online submissions for Add One Row to Tree.
"""
