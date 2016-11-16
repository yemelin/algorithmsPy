class Node:
    def __init__(self, value):
        self.value = value
        self.children = None

    def addNode(self, node):
        if not (self.children):
            self.children = []
        self.children.append(node)

    def isLeaf(self):
        return (self.children==None or len(self.children)==0)