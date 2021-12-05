x= [20,18,12,8,5,-2]
def insertion_sort(x):
    for i in range(len(x)):
        j = i - 1
        temp = x[i]
        while j >= 0 and temp < x[j]:
            x[j + 1] = x[j]
            j = j - 1
            x[j + 1] = temp
    return x 
    
# print(insertion_sort([2,3,5,7,13,11]))
