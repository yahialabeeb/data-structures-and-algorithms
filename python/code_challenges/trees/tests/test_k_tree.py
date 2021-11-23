import pytest
from trees.tree_fizz_buzz import K_tree , Node,fizz_buzz_tree
@pytest.fixture
def create():
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
    return ktree   


def test_fizz_buzz(create):
    actual = fizz_buzz_tree(create).breadth_first_K_tree() 
    excepted = ['1', '2', 'fuzz', '4', 'fuzzbuzz', 'buzz', 'buzz', '7']
    assert actual == excepted

def test_new_not_modifying(create):
    actual = fizz_buzz_tree(create).breadth_first_K_tree() 
    excepted = create.breadth_first_K_tree() 
    assert actual != excepted

def test_empty_ktree():
    ktree=K_tree()
    with pytest.raises(Exception) as excinfo:
        fizz_buzz_tree(ktree)
    assert "Empty tree" == str(excinfo.value)

def test_not_number_values():
    first_n =Node(1)
    first_n.child_array.append(Node("f"))
    first_n.child_array.append(Node(2))
    ktree=K_tree(first_n)
    with pytest.raises(Exception) as excinfo:
        fizz_buzz_tree(ktree)
    assert "must be real number, not str" == str(excinfo.value)