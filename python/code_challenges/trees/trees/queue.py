class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self,val):
        node=Node(val)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node 


    def dequeue(self):
        if not self.front:
            raise Exception ("empty queue")
        temp = self.front
        self.front = self.front.next
        return temp.value

    def peek(self):
        if not self.front:
            raise Exception ("empty queue")
        return self.front.value

    def is_empty(self):
        return not self.front
    
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
