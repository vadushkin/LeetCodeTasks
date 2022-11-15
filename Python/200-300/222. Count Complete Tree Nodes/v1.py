from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lst = []

        def dfs(node):
            if node is None:
                return

            lst.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return len(lst)


def main():
    s = Solution()
    print(s.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 217 ms Beats 17.28%
   Memory 21.3 MB Beats 97.92%

2. Runtime 119 ms Beats 77.38%
   Memory 21.3 MB Beats 97.92%
"""
