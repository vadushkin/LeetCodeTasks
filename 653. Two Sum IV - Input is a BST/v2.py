from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack, seen = [root], set()

        while stack:
            curr = stack.pop()
            if k - curr.val in seen:
                return True
            seen.add(curr.val)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False


def main():
    s = Solution()
    print(s.findTarget(TreeNode(5, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(7, right=TreeNode(6))), 9))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 197 ms, faster than 23.93% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 16.4 MB, less than 82.46% of Python3 online submissions for Two Sum IV - Input is a BST.

2. Runtime: 157 ms, faster than 51.52% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 16.3 MB, less than 82.46% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
