# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        result = []

        def dfs(node):
            if not node:
                return
            if type(node) == list:
                for i in node:
                    result.append(i.val)
                    dfs(i.children)
            if type(node) != list:
                result.append(node.val)
                dfs(node.children)

        dfs(root)
        return result


def main():
    s = Solution()
    print(s.preorder(Node(1, [Node(2, Node(5)), Node(3), Node(4)])))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 60 ms, faster than 82.84% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.3 MB, less than 17.45% of Python3 online submissions for N-ary Tree Preorder Traversal.

2. Runtime: 106 ms, faster than 12.65% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.3 MB, less than 17.45% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
