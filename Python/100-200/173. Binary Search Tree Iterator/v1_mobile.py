class BSTIterator:
    def init(self, root):
        self.g = self.iterate(root)
        self.advance()

    
    def hasNext(self):
        return self.cur is not None

    
    def next(self):
        temp = self.cur
        self.advance()
        return temp
    
    def advance(self):
        try:
            self.cur = next(self.g)
        except StopIteration:
            self.cur = None
    
    def iterate(self, node):
        if node is None:
            return
        yield from self.iterate(node.left)
        yield node.val
        yield from self.iterate(node.right)
