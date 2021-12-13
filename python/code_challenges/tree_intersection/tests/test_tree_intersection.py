from tree_intersection import __version__
import pytest 
from tree_intersection.tree_intersection import tree_intersection, Node,Binary_tree


@pytest.fixture
def testing():
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
# second tree defining
    first_n2 =Node(1)
    second_n2 = Node(2)
    third_n2 = Node(3)
    first_n2.left = second_n2
    first_n2.right = third_n2
    second_n2.left=Node(4)
    second_n2.right = Node(5)
    third_n2.left = Node(6)
    third_n2.right = Node(8)
    binary_tree2=Binary_tree(first_n2)
    return [binary_tree,binary_tree2]
def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection(testing):
    assert tree_intersection(testing[1],testing[0]) == [4, 5, 2, 6, 3, 1]