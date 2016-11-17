'''
Created on Nov 18, 2016

@author: vvy
'''
from algo.stack.stack import Stack

class DualStackQueue():
    
    def __init__(self):
        self.__in = Stack()
        self.__out = Stack()
        
    def __exchange(self, src, dest):
        while not src.empty():
            dest.push(src.pop())
        
    def enqueue (self, value):
        if not self.__out.empty():
            self.__exchange(self.__out, self.__in)
        self.__in.push(value)
    
    def dequeue(self):
        if not self.__in.empty():
            self.__exchange(self.__in, self.__out)
        return self.__out.pop()
    
    def size(self):
        return self.__in.size()+self.__out.size()
    
