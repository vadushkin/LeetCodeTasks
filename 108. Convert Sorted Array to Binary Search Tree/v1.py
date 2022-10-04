from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(nums[mid_node], self.sortedArrayToBST(nums[:mid_node]),
                        self.sortedArrayToBST(nums[mid_node + 1:]))


def main():
    s = Solution()
    print(s.sortedArrayToBST([0, 1, 2, 3, 4, 5, 6, 7, 8]))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 155 ms, faster than 22.10% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.7 MB, less than 31.68% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

2. Runtime: 162 ms, faster than 14.65% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 82.50% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""
