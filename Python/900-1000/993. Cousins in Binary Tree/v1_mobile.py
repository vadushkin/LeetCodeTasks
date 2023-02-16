class Solution:

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        queue = [(root, None)]

        while queue:

            newQueue = []

            xParent = None

            yParent = None

            for node, parent in queue:

                if node.val == x:

                    xParent = parent

                elif node.val == y:

                    yParent = parent

                if xParent and yParent:

                    return xParent != yParent

                if node.left:

                    newQueue.append((node.left, node))

                if node.right:

                    newQueue.append((node.right, node))

            queue = newQueue

        return False
