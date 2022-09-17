from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root):
        def dfs(node):
            nonlocal ans
            if node is None:
                return
            dictionary[str(node.val)] += 1
            if node.left is None and node.right is None:
                c = 0
                for i in dictionary:
                    if dictionary[i] % 2 != 0:
                        c += 1
                if c <= 1:
                    ans += 1
            dfs(node.left)
            dfs(node.right)
            dictionary[str(node.val)] -= 1

        dictionary = defaultdict(lambda: 0)
        ans = 0
        dfs(root)
        return ans


def main():
    s = Solution()
    print(s.pseudoPalindromicPaths(
        TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(1)), right=TreeNode(3, right=TreeNode(3)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 2670 ms, faster than 5.30% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 86 MB, less than 35.51% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.

2. Runtime: 2529 ms, faster than 5.30% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 86.1 MB, less than 27.10% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
"""
