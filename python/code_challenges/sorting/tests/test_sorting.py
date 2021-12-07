from sorting import __version__
from sorting.quicks_sort import quick_sort

def test_version():
    assert __version__ == '0.1.0'

def test_quick_sort_Reverse_sorted():
    x = [20,18,12,8,5,-2]
    quick_sort(x,0,5)
    actual = x
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_quick_sort_Few_uniques():
    x = [5,12,7,5,5,7]
    quick_sort(x,0,5)
    actual = x
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_quick_sort_nearly_sorted():
    x = [2,3,5,7,13,11]
    quick_sort(x,0,5)
    actual = x
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected