import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        res = 0
        while queue:
            node = queue.popleft()
            if node:
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val
                queue.append(node.left)
                queue.append(node.right)

        return res


def main():
    s = Solution()
    print(s.sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 63 ms, faster than 28.67% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.7 MB, less than 72.09% of Python3 online submissions for Sum of Left Leaves.

2. Runtime: 37 ms, faster than 88.58% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 14.2 MB, less than 90.53% of Python3 online submissions for Sum of Left Leaves.
"""
