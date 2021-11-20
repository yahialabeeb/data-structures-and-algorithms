import pytest
from trees import __version__
from trees.trees import Binary_search_tree, Binary_tree, Node

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



