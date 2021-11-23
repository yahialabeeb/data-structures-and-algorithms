from trees.queue import Queue
from trees.trees import Binary_tree
from trees.trees import binary_tree
def breadth_first(tree:Binary_tree):
    
    if not tree.root:
        raise Exception ("Empty tree")

    queue = Queue()
    list_result =[]
    queue.enqueue(tree.root)
    
    current = queue.front
    while current :
        if current.value.left:
            queue.enqueue(current.value.left)
        if current.value.right:   
            queue.enqueue(current.value.right)
        list_result.append(queue.dequeue().value)
        current = queue.front
    return list_result

# print(breadth_first(binary_tree))