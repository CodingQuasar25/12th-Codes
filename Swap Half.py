def swaphalf(x):
    l=len(x)//2
    for i in range(l):
        x[i],x[len(x)+i-l]=x[len(x)+i-l],x[i]
    return x
x=[1,2,3,4,5,6,7]
print(swaphalf(x))
