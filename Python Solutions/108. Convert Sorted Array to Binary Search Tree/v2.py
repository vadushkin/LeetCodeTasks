from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def solve(left, right):
            if left > right:
                return None
            m = (left + right) // 2
            return TreeNode(nums[m], solve(left, m - 1), solve(m + 1, right))

        return solve(0, len(nums) - 1)


def main():
    s = Solution()
    print(s.sortedArrayToBST([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 65 ms, faster than 92.98% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 31.68% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

2. Runtime: 71 ms, faster than 87.15% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.5 MB, less than 82.50% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""
