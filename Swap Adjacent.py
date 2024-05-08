def swapadj(x):
    for i in range(1,len(x),2):
        x[i],x[i-1]=x[i-1],x[i]
    return x
x=[1,2,3,4,5,6]
print(swapadj(x))
