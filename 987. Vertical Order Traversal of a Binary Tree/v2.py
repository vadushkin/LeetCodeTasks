from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        q, table, ans = deque([(root, 0, 0)]), defaultdict(list), []

        while q:
            for _ in range(len(q)):
                node, x, y = q.popleft()

                table[x].append((abs(y), node.val))

                if node.left: q.append((node.left, x - 1, y - 1))
                if node.right: q.append((node.right, x + 1, y - 1))

        for key in sorted(table.keys()):
            ans.append([v[1] for v in sorted(table[key])])

        return ans


def main():
    s = Solution()
    print(s.verticalTraversal(
        TreeNode(val=32, left=TreeNode(val=1, left=TreeNode(), right=TreeNode(val=23)),
                 right=TreeNode(val=4, left=TreeNode(val=21)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 57 ms, faster than 41.65% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.2 MB, less than 28.65% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.

2. Runtime: 53 ms, faster than 53.00% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.2 MB, less than 72.74% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
"""
