class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
            self.head = node
            self.count += 1
        else:
            self.head = node

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
            # output = f" => {self.head.value}"
            current = self.head
            while current:
                output += f" => {current.value}"
                current = current.next
            output += " => None"
            return output
        else:
            output = "Empty"
            return output

    def insert_before(self, val, new_val):
        node = Node(new_val)
        if self.head.value == val:
            node.next = self.head
            self.head = node
        else:
            current = self.head

            while current:
                if val == current.next.value:
                    node.next = current.next
                    current.next = node
                    self.count += 1
                    break
                current = current.next

    def insert_after(self, val, new_val):
        node = Node(new_val)
        current = self.head
        while current:
            if val == current.value:
                node.next = current.next
                current.next = node
                self.count += 1
                break
            current = current.next

    def kthFromEnd(self, k):
        current = self.head
        if k < 0:
            return "negative k"
        elif self.count >= k:
            for i in range(self.count - k):
                current = current.next
            return current.value
        else:
            raise Exception