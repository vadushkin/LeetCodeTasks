from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node = root

        while True:
            if val > node.val:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break

        return root


def main():
    s = Solution()
    print(s.insertIntoBST(TreeNode(4, TreeNode(2, TreeNode(1)), TreeNode(6, TreeNode(7))), 5))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 149 ms Beats 20.50% 
   Memory 17 MB Beats 43.38%

2. Runtime 129 ms Beats 93.49% 
   Memory 17 MB Beats 43.38%
"""
