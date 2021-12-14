# from .linkedlist import Linked_list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.count = 0


    def append(self, value):
        node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next

            current.next = node
        else:
            self.head = node
        self.count += 1

    def include(self, value):

        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        return False

    def __str__(self):
        if self.head:
            output = "head"
            current = self.head
            while current:
                output += f" => {current.value}"
                current = current.next
            output += " => None"
            return output
        else:
            output = "Empty"
            return output
            

class Hash_table():
    def __init__(self,size = 1024):
        self.size = size
        self.arr = [None]*size


    def add(self,key,value):
        idx = self.hash(key)
        if not self.arr[idx]:  
            self.arr[idx] = Linked_list()
        self.arr[idx].append((key,value))


    def contain(self,key):
        idx = self.hash(key)
        if self.arr[idx]:
            current = self.arr[idx].head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False


    def get(self,key):
        idx = self.hash(key)
        if self.arr[idx]:
            current = self.arr[idx].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        return None
        

    def hash(self,key):
        idx = 0
        for ch in key :
            idx += ord(ch)
        idx = idx * 11 % self.size
        return idx


# hass = Hash_table(100)
# hass.add("yahia",25)
# # print(hass.get("yahia"))
# # print(hass.contain("yahia"))