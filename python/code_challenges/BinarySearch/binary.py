a, b = [4, 8, 15, 16, 23, 42], 12


def binary(a, b):
    j = len(a)
    c = 0
    while(True):
        if j - c > 2:
            if a[int((j+c)/2)] > b:
                j = int((j+c)/2)+1
                print(j, "544")
            elif a[int((j+c)/2)] < b:
                c = int((j+c)/2)
                print(j, "l")
            else:
                j = int((j+c)/2)
                return j
        else:
            j = -1
            return j


print(binary(a, b))
