from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


def main():
    s = Solution()
    print(s.leafSimilar(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                                 TreeNode(1, TreeNode(9), TreeNode(8))),
                        TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)),
                                 TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 66 ms Beats 36.5%
   Memory 14 MB Beats 46.25%

2. Runtime 30 ms Beats 96.57%
   Memory 14 MB Beats 9.82%
"""
