from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)


def main():
    s = Solution()
    print(s.minDepth(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1461 ms, faster than 11.77% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 59.1 MB, less than 5.20% of Python3 online submissions for Minimum Depth of Binary Tree.

2. Runtime: 1902 ms, faster than 5.02% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 60.1 MB, less than 5.20% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
