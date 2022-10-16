class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> list[int]:

        def dfs(node, list_numbers):

            if node is None:
                return list_numbers

            if node.val in list_numbers:
                list_numbers[node.val] += 1
            else:
                list_numbers[node.val] = 1

            if node.left is not None:
                dfs(node.left, list_numbers)
            if node.right is not None:
                dfs(node.right, list_numbers)

            return list_numbers

        lst = dict()
        dfs(root, lst)
        m = max(lst.values())
        return [i for i, v in lst.items() if (v == m)]


def main():
    s = Solution()
    print(s.findMode(TreeNode(1, right=TreeNode(2, TreeNode(2, TreeNode(1))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 111 ms, faster than 43.93% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.5 MB, less than 16.94% of Python3 online submissions for Find Mode in Binary Search Tree.

2. Runtime: 87 ms, faster than 69.21% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 18.5 MB, less than 16.94% of Python3 online submissions for Find Mode in Binary Search Tree.
"""
