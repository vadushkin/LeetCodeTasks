class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, r: TreeNode, s: int) -> list[list[int]]:
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
        return a


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 67 ms, faster than 57.97% of Python3 online submissions for Path Sum II.
Memory Usage: 15.6 MB, less than 72.57% of Python3 online submissions for Path Sum II.

2. Runtime: 76 ms, faster than 41.07% of Python3 online submissions for Path Sum II.
Memory Usage: 15.6 MB, less than 72.57% of Python3 online submissions for Path Sum II.
"""
