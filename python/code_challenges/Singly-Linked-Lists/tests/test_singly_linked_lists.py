from singly_linked_lists import __version__
from singly_linked_lists.singly_linked_list import Linked_list,Node

import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def ll():
    ll = Linked_list()
    ll.insert(1)
    ll.append(2)
    ll.append("man")
    return ll


# 1.Can successfully instantiate an empty linked list:
def test_empty():
    ll = Linked_list()
    expected = None
    actual = ll.head
    assert expected == actual

# 2.Can properly insert into the linked list
# 3.The head property will properly point to the first node in the linked list
# 4.Can properly insert multiple nodes into the linked list
def test_insert_and_head(ll):
    expected1 = 1
    actual1 = ll.head.value
    assert expected1 == actual1
    expected2 = 2
    actual2 = ll.head.next.value
    assert expected2 == actual2



# 5.Will return true when finding a value within the linked list that exists
def test_include(ll):
    # ll = Linked_list()
    expected = True
    actual = ll.include(1)
    assert expected == actual

# 6.Will return false when searching for a value in the linked list that does not exist

def test_not_include(ll):
    # ll = Linked_list()
    expected = False
    actual = ll.include(3)
    assert expected == actual

# 7.Can properly return a collection of all the values that exist in the linked list
def all_values(ll):
    expected = "head => 1 => 2 => man => None"
    actual = ll.__str__()
    assert expected == actual