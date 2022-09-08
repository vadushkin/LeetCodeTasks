# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children)
        return output[::-1]


def main():
    s = Solution()
    # print(s.postorder(Node()))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 100 ms, faster than 19.22% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16 MB, less than 98.26% of Python3 online submissions for N-ary Tree Postorder Traversal.

2. Runtime: 100 ms, faster than 19.22% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 16 MB, less than 86.31% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
