# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = []

        def dfs(root, target, prev_sum, sum_list):
            if not root:
                return

            prev_sum += root.val
            sum_list.append(root.val)

            if prev_sum == target and root.left is None and root.right is None:
                res.append(sum_list[:])

            dfs(root.left, target, prev_sum, sum_list)
            dfs(root.right, target, prev_sum, sum_list)
            sum_list.pop()

        dfs(root, targetSum, 0, [])
        if res:
            return True
        return False


def main():
    s = Solution()
    print(s.hasPathSum(
        TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=9, left=TreeNode(val=7), right=TreeNode(val=2))),
                 right=TreeNode(val=8, left=TreeNode(val=13),
                                right=TreeNode(val=4, left=TreeNode(val=5), right=TreeNode(val=1)))), 20))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 90 ms, faster than 11.05% of Python3 online submissions for Path Sum.
Memory Usage: 15 MB, less than 56.76% of Python3 online submissions for Path Sum.

2. Runtime: 58 ms, faster than 68.91% of Python3 online submissions for Path Sum.
Memory Usage: 15.2 MB, less than 15.86% of Python3 online submissions for Path Sum.
"""
