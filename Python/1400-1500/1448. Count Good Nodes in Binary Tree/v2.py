class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, cur_max):
            if not node:
                return
            if node.val >= cur_max:
                count[0] += 1
                cur_max = node.val
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)

        count = [0]
        dfs(root, root.val)

        return count[0]


def main():
    s = Solution()
    print(s.goodNodes(TreeNode(val=3, left=TreeNode(val=1, left=TreeNode(val=3)),
                               right=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=5)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 486 ms, faster than 20.69% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.6 MB, less than 46.30% of Python3 online submissions for Count Good Nodes in Binary Tree.

2. Runtime: 559 ms, faster than 6.37% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.5 MB, less than 87.02% of Python3 online submissions for Count Good Nodes in Binary Tree.
"""
