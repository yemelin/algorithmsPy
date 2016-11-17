from stack import Stack

def reverse(input):
    ret = []
    if (input):
        s = Stack()
        for item in input:
            s.push(item)
        while not s.empty():
            ret.append(s.pop().value)
    return ret

left = "([{"
right = ")]}"
brackets = left+right

def __isMatch(l,r):
    return left.index(l)==right.index(r)

def isBalanced(input):
    if (not input or len(input)==0):
        return True
    s = Stack()
    for c in input:
        if c in left:
            s.push(c)
        elif c in right:
            if s.empty() or not __isMatch(s.pop(),c):
                return False
    return s.empty()

#print reverse('abc')