from trees.node import Node

def load(dic):
    if (not dic) or len(dic)!=1 or (not dic.has_key("root")):
        return None
    root = Node("root")
    _addTree(root,dic["root"])
    return root


def _addTree(node, tree):
    if (tree==None or len(tree)==0):
        return
    for (k,v) in tree.items():
        newNode = Node(k)
        node.addNode(newNode)
        _addTree(newNode,v)

def action(node):
    print node.value,

#depth first search
def traverseDS(tree):
    action(tree)
    if not (tree.isLeaf()):
        for child in tree.children:
            traverseDS(child)

#mixture, depth but the children first
def _traverseBSDS(nodeList):
    if (nodeList!=None):
        for node in nodeList:
            action(node)
        for node in nodeList:
            _traverseBSDS(node.children)

def traverseBSDS(tree):
    action(tree)
    _traverseBSDS(tree.children)

#breadth first
def traverseBS(tree):
    stack = []
    stack.append(tree)
    while len(stack)>0:
        node = stack.pop()
        action(node)
        if (node.children):
            stack.extend(node.children)

d = {"root":{"1":{"2":None,"3":None},"4":{"5":{"6":None,"7":None}},"8":None,"9":None}}
tree = load(d)
print tree

traverseDS(tree)
print
traverseBSDS(tree)
print
traverseBS(tree)
print