class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        res = []
        if root is None:
            return res

        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)

        recursion(root, res)
        return res


def main():
    s = Solution()
    # print(s.postorder(Node(1)))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 107 ms, faster than 11.61% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16.4 MB, less than 18.20% of Python3 online submissions for N-ary Tree Postorder Traversal.

2. Runtime: 97 ms, faster than 23.51% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16.3 MB, less than 55.48% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
