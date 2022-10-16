# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root:
            return []

        res = []
        mapping = {}
        q = deque([(root, 0)])

        while q:
            j, k = q.popleft()

            if k not in mapping:
                mapping[k] = [j.val]
            else:
                mapping[k].append(j.val)

            if j.children:
                for i in j.children:
                    q.append((i, k + 1))

        for i in sorted(mapping.keys()):
            res.append(mapping[i])

        return res


def main():
    s = Solution()
    print(s.levelOrder(Node(1, [Node(2, Node(3)), Node(4, Node(5))])))


if __name__ == "__main__":
    main()

"""Tests:
1. Runtime: 106 ms, faster than 13.72% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16.1 MB, less than 10.93% of Python3 online submissions for N-ary Tree Level Order Traversal.

2. Runtime: 106 ms, faster than 13.72% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16.1 MB, less than 10.93% of Python3 online submissions for N-ary Tree Level Order Traversal.

3. Runtime: 102 ms, faster than 18.04% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 16 MB, less than 50.08% of Python3 online submissions for N-ary Tree Level Order Traversal.
"""
