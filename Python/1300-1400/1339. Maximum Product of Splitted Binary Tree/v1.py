import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = (10 ** 9 + 7)
        subtreeSums = set()

        def getSum(node):
            if not node:
                return 0
            elif not node.left and not node.right:
                subtreeSums.add(node.val)
                return node.val
            else:
                result = getSum(node.left) + getSum(node.right) + node.val
                subtreeSums.add(result)
                return result

        rootSum = getSum(root)
        idealSplit = rootSum / 2
        closestToIdeal = 0

        for possibleSum in subtreeSums:
            if math.fabs(possibleSum - idealSplit) < math.fabs(closestToIdeal - idealSplit):
                closestToIdeal = possibleSum

        return (((rootSum - closestToIdeal) % mod) * (closestToIdeal % mod)) % mod


def main():
    s = Solution()
    print(s.maxProduct(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 528 ms Beats 71.38%
   Memory 76.6 MB Beats 24.80%

2. 
"""
