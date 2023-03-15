from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        index = 0

        while stack[index]:
            stack.append(stack[index].left)
            stack.append(stack[index].right)
            index += 1

        return not any(stack[index:])


def main():
    s = Solution()
    print(s.isCompleteTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, right=TreeNode(6)))))


if __name__ == '__main__':
    main()

"""Tests:
1. Runtime 35 ms Beats 75.65% 
   Memory 13.8 MB Beats 61.14%

2. Runtime 39 ms Beats 50.9% 
   Memory 13.8 MB Beats 61.14%
"""
