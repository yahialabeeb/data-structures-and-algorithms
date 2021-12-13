from .hash_table import Hash_table

from .trees import Binary_tree, Node
def tree_intersection(first_tree:Binary_tree,second_tree:Binary_tree):
    first = first_tree.post_order()
    second = second_tree.post_order()
    # list1_as_set = set(first)
    # intersection = list1_as_set.intersection(second)
    # print(intersection)
    hash_table = Hash_table()
    result =[]
    for i in first :
        hash_table.add(str(i),1)

    for i in second:
        if hash_table.contain(str(i)):
            result.append(i)
    return result

# first_n =Node(1)
# second_n = Node(2)
# third_n = Node(3)
# first_n.left = second_n
# first_n.right = third_n
# second_n.left=Node(4)
# second_n.right = Node(5)
# third_n.left = Node(6)
# third_n.right = Node(7)
# binary_tree=Binary_tree(first_n)

# first_n2 =Node(1)
# second_n2 = Node(2)
# third_n2 = Node(3)
# first_n2.left = second_n2
# first_n2.right = third_n2
# second_n2.left=Node(4)
# second_n2.right = Node(5)
# third_n2.left = Node(6)
# third_n2.right = Node(8)
# binary_tree2=Binary_tree(first_n2)

# print(tree_intersection(binary_tree2,binary_tree))
