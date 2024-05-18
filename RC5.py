def g(l,u,n):
    import random as r
    c=[]
    while len(c)<n:
        c.append(r.randint(l,u))
    print(c)
    lsl(c)
    p(c)
def p(x):
    l=[]
    
    for i in x:
        f=0
        if i==1 or i==0:
            continue
        for j in range (2,i):
            if i%j==0:
                f+=1
        if f==0:
            l.append(i)
    if len(l)>0:
         print('The Prime Numbers Are: ',end='')
         for i in l:
             print(i,end=', ')
    else:
        print('There are no Prime Numbers')
    
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

print('Random Number Generation')
l=int(input('Enter Lower Limit:'))
u=int(input('Enter Upper Limit:'))
n=int(input('Enter Number of Random Numbers:'))
g(l,u,n)
    
