'''
Created on Nov 13, 2016

@author: vvy
'''
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    ''' basic linked list implementation
    append, insert, delete (no size)'''

class LinkedList(object):

    def __init__(self, value=None):
        if value:
            self.head = self._makeElement(value)

#to allow "overriding" the Element class
    def _makeElement(self,value):
        return Element(value)

    def _append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
#            current.next = new_element
            self._insert_after(new_element, current)
        else:
            self.head = new_element

    def _get_position(self, position):
        if (position < 1):
            return None
        current = self.head
        i = 1
        while (current and i < position):
            current = current.next
            i += 1
        return current
    
    def _insert_after(self,new_element,previous):
        new_element.next = previous.next
        previous.next = new_element

#auxiliary, assume current!=None
    def _delete_after(self,current,previous):
        if (previous):
            previous.next = previous.next.next
        else:
            self.head = self.head.next
        
    def append(self, value):
        self._append(self._makeElement(value))

    """Get an element from a particular position.
    Assume the first position is "1".
    Return "None" if position is not in the list."""
    def get_position(self, position):
        ret = self._get_position(position)
        return ret.value if ret else None

    """Insert a new node at the given position.
    Assume the first position is "1".
    Inserting at position 3 means between
    the 2nd and 3rd elements."""
    def insert(self, value, position):
        element = self._get_position(position - 1)
        if (element):        
            self._insert_after(self._makeElement(value),element)
    
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
            self._delete_after(current, previous)
