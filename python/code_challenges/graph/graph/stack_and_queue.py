
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self , val):
        temp = self.top
        self.top = Node(val)
        self.top.next = temp

    def pop(self): 
        if not self.top:
            raise Exception("Empty")
        

        temp = self.top
        self.top = temp.next
        return temp

    def peek(self):
        if not self.top:
            raise Exception("Empty")
        return self.top.value

    def is_empty(self):
        return not self.top
    
    def __str__(self):
        if self.top:
            output = "Top"
            current = self.top
            while current:
                output += f" -> {current.value}"
                current = current.next
            return output
        else:
            output = "Empty"
            return output


         
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0
    
    def enqueue(self,val):
        print(val)
        node=Node(val)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node 


    def dequeue(self):
        if not self.front:
            raise Exception ("empty queue")
        self.count = self.count - 1
        
        temp = self.front
        self.front = self.front.next
        return temp.value

    def peek(self):
        if not self.front:
            raise Exception ("empty queue")
        return self.front.value

    def is_empty(self):
        return not self.front
    
    def __len__(self):
        return self.count
    
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

