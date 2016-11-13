'''
Created on Nov 13, 2016

@author: vvy
'''
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
    def get_position(self, position):
        if (position < 1):
            return None
        current = self.head
        i = 1
        while (current and i < position):
            current = current.next
            i += 1
        return current
    
    def __insert_after(self,new_element,previous):
        new_element.next = previous.next
        previous.next = new_element
                    
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
    def insert(self, new_element, position):
        element = self.get_position(position - 1)
        if (element and new_element):        
            self.__insert_after(new_element,element)
    
    def __delete_after(self,previous):
        if (previous):
            previous.next = previous.next.next
        else:
            self.head = self.head.next
        
        """Delete the first node with a given value."""
    def delete(self, value):
        if not self.head:
            return
        current = self.head
        previous = None
        while (current.value != value and current.next):
            previous = current
            current = current.next
        if (current.value == value):
            self.__delete_after(previous)
