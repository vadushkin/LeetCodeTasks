from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0


def main():
    s = Solution()
    print(s.maxDepth(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 45 ms, faster than 91.43% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 17.6 MB, less than 23.56% of Python3 online submissions for Maximum Depth of Binary Tree.

2. Runtime: 91 ms, faster than 16.56% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 17.7 MB, less than 23.56% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
