from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.mode = None

    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        self.mode = 0
        d = {}
        ret = []

        self.traverse(root, d)

        for node, count in d.items():
            if count == self.mode:
                ret.append(node)

        return ret

    def traverse(self, root: TreeNode, d: dict):
        if not root:
            return

        d[root.val] = d.get(root.val, 0) + 1
        self.mode = max(self.mode, d[root.val])
        self.traverse(root.left, d)
        self.traverse(root.right, d)


def main():
    s = Solution()
    print(s.findMode(TreeNode(1, right=TreeNode(2, TreeNode(2)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 136 ms, faster than 15.90% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.6 MB, less than 16.94% of Python3 online submissions for Find Mode in Binary Search Tree.

2. Runtime: 129 ms, faster than 21.99% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.5 MB, less than 16.94% of Python3 online submissions for Find Mode in Binary Search Tree.
"""
