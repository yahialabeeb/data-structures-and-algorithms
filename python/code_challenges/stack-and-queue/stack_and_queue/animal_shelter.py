class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Animal_shelter:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, animal):
        if animal == 'cat' or animal =='dog' :
            node = Node(animal)
            if not self.rear:
                self.front = node
                self.rear = node
            else:
                self.rear.next = node
                self.rear = node 
    
    def dequeue(self, pref):
        if not self.front:
            raise Exception ("empty shelter")
        cureent = self.front
        while cureent.next:
            if cureent.next.value == pref:
                temp = pref
                cureent.next = cureent.next.next
                return temp
            cureent = cureent.next
        if cureent.next == None:
            temp = self.front
            self.front = self.front.next
            return temp.value
    def __str__(self):
        if self.front:
            output = "Front =>"
            current = self.front
            while current:
                output += f" {current.value} <="
                current = current.next
            output += " Rear"
            return output
        else:
            output = "Empty"
            return output


