import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.trees = collections.defaultdict(list)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        self.convert(root)
        return [roots[0] for roots in self.trees.values() if roots[1:]]

    def convert(self, root):
        if root:
            result = frozenset([(root.val, self.convert(root.left), self.convert(root.right))])
            self.trees[result].append(root)
            return result


def main():
    s = Solution()
    print(s.findDuplicateSubtrees(TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(2)), TreeNode(2))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 46 ms Beats 91.41% 
   Memory 16.4 MB Beats 91.96%

2. Runtime 46 ms Beats 91.41% 
   Memory 16.4 MB Beats 91.96%
"""
