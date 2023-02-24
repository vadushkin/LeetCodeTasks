from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        st = []
        res = []

        while root or st:

            while root:
                st.append(root)
                root = root.left

            root = st.pop()
            res.append(root.val)

            root = root.right

        return res


def main():
    s = Solution()
    print(s.inorderTraversal(TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7))))))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 29 ms Beats 82.56% 
   Memory 14 MB Beats 8.13%

2. Runtime 31 ms Beats 73.94% 
   Memory 13.9 MB Beats 49.72%
"""
