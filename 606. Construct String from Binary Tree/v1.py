# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ans = []

        def drf(node: TreeNode) -> None:
            if not node:
                return
            ans.append(str(node.val))
            if not node.left and not node.right:
                return
            ans.append('(')
            drf(node.left)
            ans.append(')')
            if node.right:
                ans.append('(')
                drf(node.right)
                ans.append(')')

        drf(root)
        return ''.join(ans)


def main():
    s = Solution()
    print(s.tree2str(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 115 ms, faster than 15.01% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 16.4 MB, less than 72.23% of Python3 online submissions for Construct String from Binary Tree.

2. Runtime: 97 ms, faster than 28.33% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 16.6 MB, less than 10.51% of Python3 online submissions for Construct String from Binary Tree.
"""
