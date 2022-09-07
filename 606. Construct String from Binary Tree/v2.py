class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        string = str(root.val)
        if root.left:
            string += "(" + self.tree2str(root.left) + ")"
        if root.right:
            if not root.left:
                string += "()"
            string += "(" + self.tree2str(root.right) + ")"
        return string


def main():
    s = Solution()
    print(s.tree2str(TreeNode(4, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 122 ms, faster than 12.10% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 16.4 MB, less than 72.23% of Python3 online submissions for Construct String from Binary Tree.

2. Runtime: 101 ms, faster than 24.86% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 16.5 MB, less than 30.02% of Python3 online submissions for Construct String from Binary Tree.
"""
