class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node, left_bound, cands):
            if not node:
                return left_bound
            left_bound = inorder(node.left, left_bound, cands)
            if left_bound.val > node.val:
                cands.extend([left_bound, node])
            return inorder(node.right, node, cands) if node.right else node

        cands = []
        inorder(root, TreeNode(-float('inf')), cands)
        cands[0].val, cands[-1].val = cands[-1].val, cands[0].val
