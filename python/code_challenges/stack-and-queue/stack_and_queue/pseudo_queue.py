from stack_and_queue.stack_and_queue import Stack

class Pseudo_queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self , value):
        self.stack1.push(value)


    def dequeue(self):
        current = self.stack1.top
        while current:
            current = current.next
            self.stack2.push(self.stack1.pop())
              
        temp = self.stack2.pop()
        current = self.stack2.top
        while current:
            current = current.next
            self.stack1.push(self.stack2.pop())
        return temp

    def __str__(self):
        output= "Rear <= "
        current = self.stack1.top
        while current:
            output += f"{current.value} <= "
            current = current.next
        output +="Front" 
        return output
queue = Pseudo_queue()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.enqueue(3)
print(queue)
