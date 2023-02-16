class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):

            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)

        return dfs(root)
