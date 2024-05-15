def g(l,u):
    import random as r
    print(r.randint(l,u))
def p(l,u):
    for i in range (l,u):
        f=0
        if i==1 or i==0:
            continue
        for j in range (2,i):
            if i%j==0:
                f+=1
        if f==0:
            print(i,end=' ')
    print()
def lsl(x):
    c=x[0]
    sl=0
    for i in x:
        if i>c:
            c=i
    for i in x:
        if i>sl and i!=c:
            sl=i
    print('The Second Largest Number:',sl)
    print('The Largest Number:',c)
    p(sl,c)
while True:
    x=int(input('1,Generate random number:\n2.Prime Number Generator:\n3.Largest and Second Largest Number in a list:\n4.Exit\nEnter Choice:'))
    if x==1:
        l=int(input('Enter Lower Limit:'))
        u=int(input('Enter Upper Limit:'))
        g(l,u)
    elif x==2:
        l=int(input('Enter Lower Limit:'))
        u=int(input('Enter Upper Limit:'))
        p(l,u)
    elif x==3:
        x=eval(input('Enter List of Numbers:'))
        lsl(x)
    elif x==4:
        break
    

