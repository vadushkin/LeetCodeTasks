from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        level_count = defaultdict(int)
        level_sum = defaultdict(int)

        def dfs(node=root, level=0):
            if not node:
                return
            level_count[level] += 1
            level_sum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs()
        return [level_sum[i] / level_count[i] for i in range(len(level_count))]


def main():
    s = Solution()
    print(s.averageOfLevels(TreeNode(val=3, left=TreeNode(val=9),
                                     right=TreeNode(val=20, left=TreeNode(val=15),
                                                    right=TreeNode(val=7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 54 ms, faster than 92.06% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 17.2 MB, less than 8.79% of Python3 online submissions for Average of Levels in Binary Tree.

2. Runtime: 139 ms, faster than 5.06% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 17.2 MB, less than 8.79% of Python3 online submissions for Average of Levels in Binary Tree.
"""
