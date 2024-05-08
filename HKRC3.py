def fact(x):
    j=1
    for k in range (1,x+1):
        j*=k
    return j
def fibo(n):
    a,b=-1,1
    for i in range (n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
    
while True:
    opt=int(input('1.Factorial\n2.Fibonacci Series\n3.Exit\nEnter Choice:'))
    if opt==1:
        n=int(input('Enter number to get factorial:'))
        print('The factorial of',n,'is',fact(n))
    elif opt==2:
        n=int(input('Enter no. of Fibonacci series:'))
        fibo(n)
    elif opt==3:
        break
