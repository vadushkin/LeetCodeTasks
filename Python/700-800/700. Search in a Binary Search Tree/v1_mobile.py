class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        trav = root

        while trav:

            if trav.val == val:

                return trav

            elif trav.val < val:

                trav = trav.right

            else:

                trav = trav.left
