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
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


def main():
    s = Solution()
    print(s.minDepth(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 674 ms, faster than 81.45% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 54.7 MB, less than 42.33% of Python3 online submissions for Minimum Depth of Binary Tree.

2. Runtime: 1513 ms, faster than 9.10% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 54.6 MB, less than 53.04% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
