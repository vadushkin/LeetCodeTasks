# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = 0

        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node is not None:
                path = path ^ (1 << node.val)
                if node.left is None and node.right is None:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count


def main():
    s = Solution()
    print(s.pseudoPalindromicPaths(
        TreeNode(1, left=TreeNode(2, left=TreeNode(2), right=TreeNode(1)), right=TreeNode(5, right=TreeNode(5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2307 ms, faster than 5.92% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 50.4 MB, less than 95.95% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.

2. Runtime: 809 ms, faster than 97.82% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 50.3 MB, less than 98.44% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
"""
