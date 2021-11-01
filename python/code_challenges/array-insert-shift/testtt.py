x= [1,2,3]
y=23

def tet(x,y):
    x.append(y)
    j = len(x)
    idx = int(j/2)+1
    for i in reversed(range(idx,j)):
        x[i],x[i-1]=x[i-1],x[i]

tet(x,y)
print(x)

