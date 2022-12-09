"""Given the root of a binary tree,
find the maximum value v for which there exist different
nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either:
any child of a is equal to b or any child of a is an ancestor of b.

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105
"""
