class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def contains_one(node: TreeNode) -> bool:
            if not node:
                return False
            left_content = contains_one(node.left)
            right_content = contains_one(node.right)
            if not left_content:
                node.left = None
            if not right_content:
                node.right = None
            return node.val or left_content or right_content

        return root if contains_one(root) else None


def main():
    s = Solution()
    print(s.pruneTree(TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=0, left=None, right=None),
                                                    right=TreeNode(val=0, left=None, right=None)),
                               right=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                                              right=TreeNode(val=1, left=None, right=None)))
                      ))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 24.06% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 14 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.

2. Runtime: 53 ms, faster than 42.07% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 14 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.
"""
