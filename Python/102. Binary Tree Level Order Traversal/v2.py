from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans


def main():
    s = Solution()
    print(s.levelOrder(TreeNode(val=3, left=TreeNode(val=9),
                                right=TreeNode(val=20, left=TreeNode(val=15),
                                               right=TreeNode(val=7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 64 ms, faster than 27.17% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.2 MB, less than 84.78% of Python3 online submissions for Binary Tree Level Order Traversal.

2. Runtime: 51 ms, faster than 59.74% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.2 MB, less than 52.84% of Python3 online submissions for Binary Tree Level Order Traversal.
"""
