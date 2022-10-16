from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        ans = []

        def dfs(node, res=""):
            if node is None:
                return
            if not node.left and not node.right:
                res += f"{node.val}"
                ans.append(res)
            res += f"{node.val}->" if node.right or node.left else f"{node.val}"
            dfs(node.left, res)
            dfs(node.right, res)

        dfs(root)
        return ans


def main():
    s = Solution()
    print(s.binaryTreePaths(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5, TreeNode(10)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 51 ms, faster than 63.17% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.6 MB, less than 99.88% of Python3 online submissions for Binary Tree Paths.

2. Runtime: 62 ms, faster than 35.68% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.9 MB, less than 29.76% of Python3 online submissions for Binary Tree Paths.
"""
