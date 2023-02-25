from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], count=0) -> int:
        return count if not root else max(self.maxDepth(root.left, count + 1), self.maxDepth(root.right, count + 1))


def main():
    s = Solution()
    print(s.maxDepth(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 43 ms Beats 69.58% 
   Memory 16.4 MB Beats 19.4%

2. Runtime 41 ms Beats 79.2% 
   Memory 16.5 MB Beats 19.4%
"""
