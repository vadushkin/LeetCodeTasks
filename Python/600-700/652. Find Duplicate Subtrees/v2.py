import collections
from functools import lru_cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs_tuplify(node):
            if node:
                tuple_ = node.val, dfs_tuplify(node.left), dfs_tuplify(node.right)
                trees[tuple_].append(node)
                return tuple_

        trees = collections.defaultdict(list)
        dfs_tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]


def main():
    s = Solution()
    print(s.findDuplicateSubtrees(TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(2)), TreeNode(2))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 91 ms Beats 28.35% 
   Memory 16.6 MB Beats 75%

2. Runtime 96 ms Beats 26.67% 
   Memory 16.5 MB Beats 86.50%
"""
