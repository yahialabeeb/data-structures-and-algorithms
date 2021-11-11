from singly_linked_lists.singly_linked_list import Linked_list, Node


def is_pal(ll):
    current = ll.head
    listll = [x for x in range(ll.count)]
    for i in listll:
        listll[i] = current.value
        current = current.next
        
    j = len(listll)
    count_right = 0
    for i in range(int(j/2)):
        if listll[i] == listll[j-1-i]:
            count_right += 1
            print(count_right)
    if count_right == int(j/2):
        return True
    return False

ll = Linked_list()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(1)
print(is_pal(ll))