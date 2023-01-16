from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, buf=""):
            if not node:
                return

            if not node.left and not node.right:
                cval = buf + str(node.val)
                self.total += int(cval, 2)
            else:
                tmp = buf + str(node.val)
                dfs(node.left, tmp)
                dfs(node.right, tmp)

        dfs(root)

        return self.total % (10 ** 9 + 7)


def main():
    s = Solution()
    print(s.sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 45 ms Beats 60.51% 
   Memory 14.2 MB Beats 78.27%

2. Runtime 36 ms Beats 91.36%
   Memory 14.2 MB Beats 78.27%
"""
