from blog import insertion_sort
t1 =[20,18,12,8,5,-2]
t2= [5,12,7,5,5,7]
t3 = [2,3,5,7,13,11]
def test1():
    actual = insertion_sort(t1)
    expected = [-2, 5, 8, 12, 18, 20]
    return actual == expected

def test2():
    actual = insertion_sort(t2)
    expected = [5, 5, 5, 7, 7, 12]
    return actual == expected

def test3():
    actual = insertion_sort(t3)
    expected = [2, 3, 5, 7, 11, 13]
    return actual == expected

print(test1())
print(test2())
print(test3())
