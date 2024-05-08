def negpos(x):
    for i in range (len(x)):
        if x[i]<0:
            for j in range(i):
                if x[j]<0:
                    continue
                else:
                    x[i],x[j]=x[j],x[i]
    return x
x=[-5,3,2,-1,6,-4,7,-3]
print(negpos(x))
