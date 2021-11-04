class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None

    def insert(self,value):
        node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node                
        else:
            self.head = node
            

    def include(self,value):

        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        return False
        
         

    def __str__(self):
        if self.head:
            output = "head"
            # output = f" => {self.head.value}"
            current = self.head
            while current :
                output += f" => {current.value}"
                current = current.next
            output += " => None"
            return output
        else:
            output = "Empty"
            return output

        