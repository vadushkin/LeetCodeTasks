# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
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
        return res


def main():
    s = Solution()
    print(s.pathSum(TreeNode(val=5, left=TreeNode(val=4,
                                                  left=TreeNode(val=11, left=TreeNode(val=7, left=None, right=None),
                                                                right=TreeNode(val=2, left=None, right=None)),
                                                  right=None),
                             right=TreeNode(val=8, left=TreeNode(val=13, left=None, right=None),
                                            right=TreeNode(val=4, left=TreeNode(val=5, left=None, right=None),
                                                           right=TreeNode(val=1, left=None, right=None))))
                    , 22))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 81 ms, faster than 31.78% of Python3 online submissions for Path Sum II.
Memory Usage: 15.5 MB, less than 72.57% of Python3 online submissions for Path Sum II.

2. Runtime: 84 ms, faster than 26.46% of Python3 online submissions for Path Sum II.
Memory Usage: 15.6 MB, less than 53.44% of Python3 online submissions for Path Sum II.
"""
