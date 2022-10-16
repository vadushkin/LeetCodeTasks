# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, r: TreeNode, s: int) -> bool:
        a, p = [], []

        def dfs(n):
            if n == None: return
            p.append(n.val)
            if (n.left, n.right) == (None, None) and sum(p) == s:
                a.append(list(p))
            else:
                dfs(n.left), dfs(n.right)
            p.pop()

        dfs(r)
        if a:
            return True
        return False


def main():
    s = Solution()
    print(s.hasPathSum(TreeNode(val=5, left=TreeNode(val=4,
                                                     left=TreeNode(val=10, left=TreeNode(val=7, left=None, right=None),
                                                                   right=TreeNode(val=2, left=None, right=None)),
                                                     right=None),
                                right=TreeNode(val=8, left=TreeNode(val=13, left=None, right=None),
                                               right=TreeNode(val=4, left=TreeNode(val=5, left=None, right=None),
                                                              right=TreeNode(val=1, left=None, right=None))))
                       , 21))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 69 ms, faster than 47.09% of Python3 online submissions for Path Sum.
Memory Usage: 15.1 MB, less than 15.86% of Python3 online submissions for Path Sum.

2. Runtime: 103 ms, faster than 5.02% of Python3 online submissions for Path Sum.
Memory Usage: 15 MB, less than 56.76% of Python3 online submissions for Path Sum.
"""
