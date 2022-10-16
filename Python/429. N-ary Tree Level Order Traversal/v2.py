# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:
        ans = []

        if not root:
            return

        def bsf(nodes):
            if not nodes:
                return

            children, nextNodes = [], []
            for node in nodes:
                children.append(node.val)
                nextNodes += node.children
            ans.append(children)
            bsf(nextNodes)

        ans.append([root.val])
        bsf(root.children)
        return ans


def main():
    pass


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 102 ms, faster than 18.04% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16.2 MB, less than 10.93% of Python3 online submissions for N-ary Tree Level Order Traversal.

2. Runtime: 75 ms, faster than 60.30% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16.1 MB, less than 10.93% of Python3 online submissions for N-ary Tree Level Order Traversal.
"""
