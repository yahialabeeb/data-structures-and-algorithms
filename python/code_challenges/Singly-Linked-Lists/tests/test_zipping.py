from singly_linked_lists import __version__
from singly_linked_lists.singly_linked_list import Linked_list, Node ,zip_lists

import pytest

@pytest.fixture
def ll():
    ll = Linked_list()
    ll.insert(1)
    ll.append(2)
    ll.append("man")
    return ll
@pytest.fixture
def ll2():
    ll2 = Linked_list()
    ll2.insert(1.5)
    ll2.append(2.5)
    ll2.append("man2")
    ll3 = Linked_list()
    ll3.insert(1.5)
    ll3.append(2.5)
    ll4 = Linked_list()
    return ll2 , ll3 , ll4


# defualt case 
def test_zip_equal(ll,ll2):
    newll = zip_lists(ll,ll2[0])
    expected = "head => 1 => 1.5 => 2 => 2.5 => man => man2 => None"
    actual = newll.__str__()
    assert expected == actual

# edge case 1 not equal  
def test_zip_not_equal(ll,ll2):
    newll = zip_lists(ll,ll2[1])
    expected = "head => 1 => 1.5 => 2 => 2.5 => man => None"
    actual = newll.__str__()
    assert expected == actual

def test_zip_not_equal2(ll,ll2):
    newll = zip_lists(ll2[1],ll)
    expected = "head => 1.5 => 1 => 2.5 => 2 => man => None"
    actual = newll.__str__()
    assert expected == actual

# edge case 2 one of them has length equal zero  
def test_zip_len_zero(ll,ll2):
    newll = zip_lists(ll,ll2[2])
    expected = "head => 1 => 2 => man => None"
    actual = newll.__str__()
    assert expected == actual