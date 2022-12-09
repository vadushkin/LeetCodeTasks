class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            if not node:
                return

            self.result = max(self.result, abs(cur_max - node.val),
                              abs(cur_min - node.val))

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)

        return self.result


def main():
    s = Solution()
    print(s.maxAncestorDiff(TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
                                     TreeNode(10, right=TreeNode(14, right=TreeNode(13))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime 47 ms Beats 83.91%
   Memory 20.1 MB Beats 32.9%

2. Runtime 74 ms Beats 57.9% 
   Memory 19.9 MB Beats 60.12%
"""
