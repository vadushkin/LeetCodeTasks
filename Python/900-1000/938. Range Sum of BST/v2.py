import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total, deque = 0, collections.deque([root])

        while deque:
            node = deque.popleft()

            if low <= node.val <= high:
                total += node.val

            if node.right:
                deque.append(node.right)
            if node.left:
                deque.append(node.left)

        return total


def main():
    s = Solution()
    print(s.rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, right=TreeNode(18))), 7, 15))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 1156 ms Beats 5.3%
   Memory 23.5 MB Beats 8.17%
   
2. Runtime 776 ms Beats 7.11%
   Memory 23.2 MB Beats 8.17%
"""
