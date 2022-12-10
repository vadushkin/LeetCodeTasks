from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        SN, M = [], 10 ** 9 + 7

        def SumTree(node):
            if node is None:
                return 0
            SN.append(node.val + SumTree(node.left) + SumTree(node.right))
            return SN[-1]

        SumTree(root)
        S, _ = SN[-1], SN.sort()
        for i, s in enumerate(SN):
            if s >= S // 2:
                return max(SN[i - 1] * (S - SN[i - 1]), SN[i] * (S - SN[i])) % M


def main():
    s = Solution()
    print(s.maxProduct(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 311 ms Beats 98.25%
   Memory 76.8 MB Beats 23.53%

2. Runtime 318 ms Beats 96.98%
   Memory 76.6 MB Beats 24.80%
"""
