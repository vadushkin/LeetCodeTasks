from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> float | int:
        max_path = float('-inf')

        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal max_path

            if not node:
                return 0

            gain_from_left = max(gain_from_subtree(node.left), 0)

            gain_from_right = max(gain_from_subtree(node.right), 0)

            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)

        return max_path


def main():
    s = Solution()
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 207 ms Beats 36.23%
   Memory 21.5 MB Beats 31.96%
   
2. Runtime 223 ms Beats 22.47% 
   Memory 21.5 MB Beats 31.96% 
"""
