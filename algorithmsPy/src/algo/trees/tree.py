from node import Node

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

def traverseDS(tree):
    action(tree)
    if not (tree.isLeaf()):
        for child in tree.children:
            traverseDS(child)

def _traverseBS(nodeList):
    if (nodeList!=None):
        for node in nodeList:
            action(node)
        for node in nodeList:
            _traverseBS(node.children)

def traverseBS(tree):
    action(tree)
    _traverseBS(tree.children)

d = {"root":{"1":{"2":None,"3":None},"4":{"5":{"6":None,"7":None}},"8":None,"9":None}}
tree = load(d)
print tree

traverseDS(tree)
print
traverseBS(tree)
print