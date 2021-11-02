x = [42,8,15,23,42]
y = 16


def tet(x, y):
    d = list(range(len(x)+1))
    j = len(d)
    idx = int(j/2)
    for i in range(j):
        if i == idx:
            d[i] = y
        elif i < idx:
            d[i] = x[i]
        else:
            d[i] = x[i-1]
    print(d)


tet(x, y)
