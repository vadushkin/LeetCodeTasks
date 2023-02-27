from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        trav = root

        while trav:
            if trav.val == val:
                return trav
            elif trav.val < val:
                trav = trav.right
            else:
                trav = trav.left


def main():
    s = Solution()
    print(s.searchBST(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5)), 2))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 81 ms Beats 57.26% 
   Memory 16.4 MB Beats 62.18%

2. Runtime 73 ms Beats 90.85% 
   Memory 16.6 MB Beats 16.45%
"""
