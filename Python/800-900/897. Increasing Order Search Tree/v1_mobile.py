class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = pre = TreeNode(None)

        curr = root

        stack = []

        

        while stack or curr:

            

            while curr:

                stack.append(curr)

                curr = curr.left

              

            curr = stack.pop()

            curr.left = None

            pre.right = curr

            pre = curr

            curr = curr.right

        

        return head.right
