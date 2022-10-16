# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                path = path ^ (1 << node.val)
                if node.left is None and node.right is None:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    preorder(node.left, path)
                    preorder(node.right, path)

        count = 0
        preorder(root, 0)
        return count


def main():
    s = Solution()
    print(s.pseudoPalindromicPaths(
        TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(1)), right=TreeNode(5, right=TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 1679 ms, faster than 27.73% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 85.5 MB, less than 58.57% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.

2. Runtime: 818 ms, faster than 97.51% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 85.8 MB, less than 43.30% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
"""
