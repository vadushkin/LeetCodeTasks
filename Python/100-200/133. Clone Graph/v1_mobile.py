class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        

        def clone(node):

            if node in old_to_new:

                return old_to_new[node]

            

            copy = Node(node.val)

            old_to_new[node] = copy

            

            for nei in node.neighbors:

                copy.neighbors.append(clone(nei))

            return copy 

        

        return clone(node) if node else None
