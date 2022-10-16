# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children[::-1])
        return output


def main():
    s = Solution()
    # print(s.preorder(Node(1, Node(2, Node(5, Node(3, Node(4)))))))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 112 ms, faster than 7.97% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16 MB, less than 97.65% of Python3 online submissions for N-ary Tree Preorder Traversal.

2. Runtime: 74 ms, faster than 61.53% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16 MB, less than 97.65% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
