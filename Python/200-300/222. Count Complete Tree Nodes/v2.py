from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        queue, total_len = deque([root]), 0

        while queue:
            node = queue.popleft()

            if node:
                total_len += 1
                queue.append(node.left)
                queue.append(node.right)

        return total_len


def main():
    s = Solution()
    print(s.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 232 ms Beats 9.71%
   Memory 21.4 MB Beats 46.74%

2. Runtime 184 ms Beats 43.5% 
   Memory 21.6 MB Beats 11.61%
"""
