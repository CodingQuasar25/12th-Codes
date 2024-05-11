def mulmat(x,y):
    c=[]
    if len(x)==len(y[0]):
        for i in range (len(x[0])):
            d=[]
            for j in range (len(y)):
                ct=0
                for k in range (len(x)):
                    ct+=x[k][i]*y[j][k]
                d.append(ct)
            c.append(d)   
    return (c)
x=eval(input('Enter 1st Nested List of Numbers: '))
y=eval(input('Enter 2nd Nested List of Numbers: '))
print(mulmat(x,y))

