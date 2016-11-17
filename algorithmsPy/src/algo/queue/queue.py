from numbers import Number

def _lessthan (x,y):
    return x<y
def _greaterthan(x,y):
    return x>y

class MinMaxQueue():

    def __init__(self):
        self.items = []
        self.lo= None
        self.hi = None

    def enqueue(self, value):
        if not isinstance(value, Number):
            raise Exception("adding a non-numeric value")
        if len(self.items)==0:
            self.hi = value
            self.lo= value
        else:
            if self.min>value:
                self.lo= value
            if self.max<value:
                self.hi = value
        self.items.append(value)

    def dequeue(self):
        ret = self.items.pop(0)
        if len(self.items)!=0:
            if (ret>=self.max()):
                self.hi = None
            if (ret<=self.min()):
                self.lo = None
        return ret

    def size(self):
        return len(self.items)

    def min(self):
        if (self.lo==None):
            self.lo = self._find(_lessthan)
        return self.lo

    def max(self):
        if (self.hi==None):
            self.hi = self.find(_greaterthan)
        return self.hi

    def find(self, cmp_func):
        ret = None
        for item in self.items:
            if ret==None or cmp_func(item, ret):
                ret = item
        return ret

