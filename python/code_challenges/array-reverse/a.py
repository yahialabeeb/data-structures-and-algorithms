array = [1,2,3]
def my_reverse_fun(input) :
    reversed = []
    for i in range(len(input)):
        reversed.append(input[(len(input)-1-i)])
    return reversed
print(my_reverse_fun(array))