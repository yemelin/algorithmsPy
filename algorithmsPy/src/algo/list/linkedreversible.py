'''
Created on Nov 14, 2016

@author: vvy
'''
from linked import LinkedList

class LinkedReversible(LinkedList):
    
    __size = 0
    def __init__(self,value):
        super(LinkedReversible,self).__init__(value)
        if self.head!=None:
            self.__size+=1
            
    def _delete_after(self, previous):
        super(LinkedReversible,self)._delete_after(previous)
        self.__size-=1
    
    def _insert_after(self, new_element, previous):
        super(LinkedReversible,self)._insert_after(new_element, previous)
        self.__size+=1
    
    def append(self, value):
        super(LinkedReversible,self).append(value)
        self.__size+=1
        
    def size(self):
        return self.__size
    
    def reverse(self):
        if (self.__size>2):
            first = self.head
            second = first.next
            third = None
            first.next = None
            while second!=None:
                third = second.next;
                second.next = first;
                first = second;
                second = third;
            self.head = first;