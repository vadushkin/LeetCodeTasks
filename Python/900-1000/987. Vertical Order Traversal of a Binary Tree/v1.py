# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        indexes = defaultdict(list)

        def dfs(node=root, level=0, index=0):
            if not node:
                return
            indexes[(level, index)].append(node.val)
            dfs(node.left, level + 1, index - 1)
            dfs(node.right, level + 1, index + 1)

        dfs()

        ans = [[] for _ in indexes]
        # sorted by columns
        sorted_list = sorted(indexes, key=lambda x: (x[1], x[0]))

        # for append index to ans [-2 == -2 - min_value (2) ] ans[0]
        min_value = 0 - sorted_list[0][1]

        for i in sorted_list:
            for j in sorted(indexes[i]):
                ans[i[1] + min_value].append(j)

        ans = [a for a in ans if a]
        return ans


def main():
    s = Solution()
    print(s.verticalTraversal(
        TreeNode(val=3, left=TreeNode(val=1, left=TreeNode(),
                                      right=TreeNode(val=2)),
                 right=TreeNode(val=4, left=TreeNode(val=2)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 79 ms, faster than 5.45% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.1 MB, less than 72.74% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.

2. Runtime: 63 ms, faster than 26.21% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.2 MB, less than 72.74% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
"""
