from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs_for_list_1(node: TreeNode) -> None:
            if node is None:
                return

            if not node.right and not node.left:
                self.list1.append(node.val)

            dfs_for_list_1(node.left)
            dfs_for_list_1(node.right)

        def dfs_for_list_2(node: TreeNode) -> None:
            if node is None:
                return

            if not node.right and not node.left:
                self.list2.append(node.val)

            dfs_for_list_2(node.left)
            dfs_for_list_2(node.right)

        dfs_for_list_1(root1)
        dfs_for_list_2(root2)

        return self.list1 == self.list2


def main():
    s = Solution()
    print(s.leafSimilar(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                                 TreeNode(1, TreeNode(9), TreeNode(8))),
                        TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)),
                                 TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))))


if __name__ == "__main__":
    main()

"""Tests: 
1. Runtime 73 ms Beats 10.84% 
   Memory 13.9 MB Beats 46.25%

2. Runtime 75 ms Beats 8.16%
   Memory 14 MB Beats 46.25%
"""
