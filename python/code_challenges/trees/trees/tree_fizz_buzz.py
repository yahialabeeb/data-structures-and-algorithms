import math
from trees.queue import Queue

class Node:
    def __init__(self,value):
        self.value = value 
        self.child_array = []
    
class K_tree:
    def __init__(self,root = None):
        self.root = root

    def breadth_first_K_tree(self):
        
        if not self.root:
            raise Exception ("Empty tree")
        
        queue = Queue()
        list_result =[]
        queue.enqueue(self.root)
        
        current = queue.front
        while current :
            for i in queue.front.value.child_array:
                queue.enqueue(i)
            list_result.append(queue.dequeue().value)
            current = queue.front
        return list_result



def fizz_buzz_tree(tree:K_tree): 
    if not tree.root:
        raise Exception("Empty tree")
    if math.isnan(tree.root.value):
        raise Exception ("must be real number, not str")
    queue = Queue()
    queue2 = Queue()
    new_tree = K_tree(Node(tree.root.value))
    current = tree.root
   

    if current.value % 3 == 0 and current.value % 5 == 0:
        new_tree.root.value = "fuzzbuzz"
    elif current.value % 3 == 0:
        new_tree.root.value = "fuzz"
    elif current.value % 5 == 0:
        new_tree.root.value = "buzz"
    else:
        new_tree.root.value = f"{current.value}"
    
    queue.enqueue(current)
    queue2.enqueue(new_tree.root)
    while current:
        temp_array = queue.front.value.child_array
        temp_array2 = queue2.front.value.child_array   
        for i in range(len(temp_array)):
            queue.enqueue(temp_array[i])
            if math.isnan(temp_array[i].value):
                raise Exception ("must be real number, not str")
            if temp_array[i].value % 3 == 0 and temp_array[i].value % 5 == 0:
                temp_array2.append(Node("fuzzbuzz"))
            elif temp_array[i].value % 3 == 0:
                temp_array2.append(Node("fuzz"))
            elif temp_array[i].value % 5 == 0:
                temp_array2.append(Node("buzz"))
            else:
               temp_array2.append(Node(f"{temp_array[i].value}"))
            queue2.enqueue(temp_array2[i])
        queue.dequeue()
        queue2.dequeue()
        current = queue.front
    return new_tree

first_n =Node(1)
second_n = Node(2)
third_n = Node(3)
first_n.child_array.append(second_n)
first_n.child_array.append(third_n)
second_n.child_array.append(Node(4))
second_n.child_array.append(Node(15))
second_n.child_array.append(Node(20))
third_n.child_array.append(Node(5))
third_n.child_array.append(Node(7))
ktree=K_tree(first_n)
print(fizz_buzz_tree(ktree).breadth_first_K_tree())
print(ktree.breadth_first_K_tree())