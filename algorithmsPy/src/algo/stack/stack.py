from list.linked import Element

#simple stack from scratch
class Stack():

    def __init__(self):
        self.__sz = 0
        self.top=None

    def push(self,value):
        element = Element(value)
        if (self.top):
            element.next=self.top
        self.top=element
        self.__sz+=1

    def pop(self):
        ret=self._peek()
        self.top = self.top.next
        self.__sz-=1
        return ret.value

    def _peek(self):
        if (self.__sz==0):
            raise Exception("stack empty")
        return self.top

    def peek(self):
        return self._peek().value

    def empty(self):
        return self.__sz==0

'''
s = Stack()
s.push(1)
s.push(2)
print s.peek()
s.pop()
print s.pop()
print s.pop()
'''