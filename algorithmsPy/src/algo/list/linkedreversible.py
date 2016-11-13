'''
Created on Nov 14, 2016

@author: vvy
'''
from linked import LinkedList

class LinkedReversible(LinkedList):
    
    __size = 0
    def __init__(self,head):
        super(LinkedReversible,self).__init__(head)
        if self.head!=None:
            self.__size+=1
            
    def delete_after(self, previous):
        super(LinkedReversible,self).delete_after(previous)
        self.__size-=1
    
    def insert_after(self, new_element, previous):
        super(LinkedReversible,self).insert_after(new_element, previous)
        self.__size+=1
    
    def append(self, new_element):
        super(LinkedReversible,self).append(new_element)
        self.__size+=1
        
    def size(self):
        return self.__size