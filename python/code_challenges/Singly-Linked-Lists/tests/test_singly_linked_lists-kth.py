from singly_linked_lists import __version__
from singly_linked_lists.singly_linked_list import Linked_list, Node

import pytest


@pytest.fixture
def ll():
    ll = Linked_list()
    ll.insert(1)
    ll.append(2)
    ll.append("man")
    return ll

# Where k is greater than the length of the linked list

# def test_kthFromEnd_greater_k(ll):

#     expected = Exception
#     actual = ll.kthFromEnd(4)
#     assert expected == actual

def test_kthFromEnd_k(ll):
# Where k and the length of the list are the same
    expected = 1
    actual = ll.kthFromEnd(2)
    assert expected == actual   

# Where k is not a positive integer
def test_kthFromEnd_negative(ll):
    
    expected = "negative k"
    actual = ll.kthFromEnd(-1)
    assert expected == actual    


# Where the linked list is of a size 1
def test_kthFromEnd_size_1():
    ll = Linked_list()
    ll.insert(1)
    expected = 1
    actual = ll.kthFromEnd(0)
    assert expected == actual  

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kthFromEnd_smaller_k(ll):
    expected = 2
    actual = ll.kthFromEnd(1)
    assert expected == actual


