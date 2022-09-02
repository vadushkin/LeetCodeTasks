# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        result = []
        level = (root,)
        while level:
            result.append(sum(node.val for node in level) / len(level))
            level = tuple(leaf for node in level for leaf in (node.left, node.right) if leaf)

        return result


def main():
    s = Solution()
    print(s.averageOfLevels(TreeNode(val=3, left=TreeNode(val=9),
                                     right=TreeNode(val=20, left=TreeNode(val=15),
                                                    right=TreeNode(val=7)))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 107 ms, faster than 12.55% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.6 MB, less than 22.03% of Python3 online submissions for Average of Levels in Binary Tree.

2. Runtime: 94 ms, faster than 27.04% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.5 MB, less than 87.46% of Python3 online submissions for Average of Levels in Binary Tree.
"""
