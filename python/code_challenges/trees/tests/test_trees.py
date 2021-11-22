import pytest
from trees import __version__
from trees.trees import Binary_search_tree, Binary_tree, Node
from trees.breadth_first import breadth_first
def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture 
def binary():
    first_n =Node(1)
    second_n = Node(2)
    third_n = Node(3)
    first_n.left = second_n
    first_n.right = third_n
    second_n.left=Node(4)
    second_n.right = Node(5)
    third_n.left = Node(6)
    third_n.right = Node(7)
    binary_tree=Binary_tree(first_n)
    return binary_tree

# Can successfully instantiate an empty tree
def test_empty_tree():
    binary_tree=Binary_tree()
    actual = binary_tree.post_order() 
    excepted = []
    assert actual == excepted

# Can successfully instantiate a tree with a single root node
def test_single_node_tree():
    binary_tree=Binary_tree(Node(2))
    actual = binary_tree.post_order() 
    excepted = [2]
    assert actual == excepted

# Can successfully add a left child and right child to a single root node
def test_single_tree():
    first_n =Node(1)
    second_n = Node(2)
    third_n = Node(3)
    first_n.left = second_n
    first_n.right = third_n
    binary_tree=Binary_tree(first_n)
    actual = binary_tree.pre_order() 
    excepted = [1,2,3]
    assert actual == excepted
    
# Can successfully return a collection from a preorder traversal
def test_preorder_tree(binary):
    actual = binary.pre_order() 
    excepted = [1, 2, 4, 5, 3, 6, 7]
    assert actual == excepted

# Can successfully return a collection from an inorder traversal
def test_inorder_tree(binary):

    actual = binary.in_order() 
    excepted = [4, 2, 5, 1, 6, 3, 7]
    assert actual == excepted
# Can successfully return a collection from a postorder traversal
def test_postorder_tree(binary):
    actual = binary.post_order() 
    excepted = [4, 5, 2, 6, 7, 3, 1]
    assert actual == excepted

# check max
def test_max_tree(binary):
    actual = binary.max() 
    excepted = 7
    assert actual == excepted


def test_breadth_first(binary):
    actual = breadth_first(binary)
    excepted = [1,2,3,4,5,6,7]
    assert actual == excepted

def test_breadth_first(binary):
    actual = breadth_first(binary)
    excepted = [1,2,3,4,5,6,7]
    assert actual == excepted

def test_not_complete_breadth_first():
    first_n =Node(1)
    second_n = Node(2)
    third_n = Node(3)
    fourth_n = Node(4)
    first_n.left = second_n
    first_n.right = third_n
    second_n.left=fourth_n
    third_n.right = Node(7)
    fourth_n.left= Node(8)
    fourth_n.right= Node(9)
    binary_tree=Binary_tree(first_n)
    actual = breadth_first(binary_tree)
    excepted = [1,2,3,4,7,8,9]
    assert actual == excepted

def test_empty_tree():
    binary_tree=Binary_tree()
    with pytest.raises(Exception) as excinfo:
        breadth_first(binary_tree)
    assert "Empty tree" == str(excinfo.value)