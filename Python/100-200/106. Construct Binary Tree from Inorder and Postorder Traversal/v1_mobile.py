class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:

            return None

        

        root = TreeNode(postorder.pop())

        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)

        root.left = self.buildTree(inorder[:inorderIndex], postorder) 

        return root
