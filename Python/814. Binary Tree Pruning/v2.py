class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        _l = self.pruneTree(root.left)
        _r = self.pruneTree(root.right)
        if root.val == 0 and _l is None and _r is None:
            return None
        else:
            root.left = _l
            root.right = _r
        return root


def main():
    s = Solution()
    print(s.pruneTree(TreeNode(val=1, left=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                                                    right=TreeNode(val=0, left=None, right=None)),
                               right=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                                              right=TreeNode(val=1, left=None, right=None)))
                      ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 63 ms, faster than 17.11% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 13.9 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.

2. Runtime: 75 ms, faster than 5.22% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 14 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.
"""
