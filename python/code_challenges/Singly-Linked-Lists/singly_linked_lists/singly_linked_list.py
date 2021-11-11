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
            raise Exception("wrong index")


def zip_lists_old(list1, list2):
    list1_current = list1.head
    list2_current = list2.head
    new_ll = Linked_list()
    while list1_current != None & list2_current != None:
        new_ll.append(list1_current.value)
        new_ll.append(list2_current.value)
        list1_current = list1_current.next
        list2_current = list2_current.next

    while list1_current:
        new_ll.append(list1_current.value)
        list1_current = list1_current.next
    while list2_current:
        new_ll.append(list2_current.value)
        list2_current = list2_current.next
    return new_ll


def zip_lists(list1, list2):
    list1_current = list1.head
    list2_current = list2.head
    while list1_current and list2_current:
        temp = list1_current.next
        temp2 = list2_current.next
        list2_current.next = temp
        list1_current.next = list2_current
        if not temp:
            temp3 = list1_current.next
        list1_current = temp
        list2_current = temp2
    while list2_current:
        temp3.next =list2_current
        list2_current =list2_current.next
    return list1
    

