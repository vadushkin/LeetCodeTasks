from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root is None or (lambda a: lambda p, q: a(a, p, q))(lambda f, l, r: (l is None and r is None) or (
                l is not None and r is not None and l.val == r.val and f(f, l.left, r.right) and f(f, l.right,
                                                                                                   r.left)))(root.left,
                                                                                                             root.right)


def main():
    s = Solution()
    print(s.isSymmetric(TreeNode(3, left=TreeNode(4), right=TreeNode(4))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 44 ms Beats 21.62% 
   Memory 13.9 MB Beats 53.36%

2. Runtime 31 ms Beats 89.28% 
   Memory 13.9 MB Beats 53.36%
"""
