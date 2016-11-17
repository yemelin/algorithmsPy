from linkedreversible import LinkedReversible
from linked import Element

#added link to the previous element
class DoublyElement(Element):
    def __init__(self, value):
        super(DoublyElement,self).__init__(value);
        self.prev=None

class DoublyLinkedReversible(LinkedReversible):

    def _makeElement(self,value):
        return DoublyElement(value)

    def _insert_after(self, new_element, previous):
        super(DoublyLinkedReversible,self)._insert_after(new_element,previous)
        new_element.prev=previous

    def _delete_after(self, current, previous):
        super(DoublyLinkedReversible,self)._delete_after(current, previous)
        if (current.next):
            current.next.prev=current.prev

    def reverse(self):
        if (self.size()>=2):
            current = self.head
            while (current):
                next = current.next
                current.next = current.prev
                current.prev = next
                self.head = current
                current = next

l = DoublyLinkedReversible(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

l.delete(3)
l.reverse()
n=l.head
while (n):
    print n.value
    n = n.next
