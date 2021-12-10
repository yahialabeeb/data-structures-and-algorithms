from sorting.marge_sort import merge_sort


def test_merge_sort_Reverse_sorted():
    x = [20,18,12,8,5,-2]
    merge_sort(x,0,5)
    actual = x
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_merge_sort_Few_uniques():
    x = [5,12,7,5,5,7]
    merge_sort(x,0,5)
    actual = x
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_merge_sort_nearly_sorted():
    x = [2,3,5,7,13,11]
    merge_sort(x,0,5)
    actual = x
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected