class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root):

            if not root:

                return

            elif root.val != self.minimum and root.val < self.sminimum:

                self.sminimum = root.val

            dfs(root.left)

            dfs(root.right)

            

        self.minimum = root.val

        self.sminimum = float('inf')

        dfs(root)

        return self.sminimum if self.sminimum != float("inf") else -1
