def power(i):
    j=1
    for k in range (i):
        j*=x
    return j
def fact(i):
    j=1
    for k in range (1,i):
        j*=k
    return j

def ser (x,n):
    s,b=0,1
    for i in range (2,2*n+1,2):
        s+=(power(i-1)/fact(i+1))*b
        b*=-1
    return(s)

def ser1 (x,n):
    s,b=0,1
    for i in range (1,2*n,2):        
        s+=(power(i)/fact(i+3))*b
        b*=-1
    return(s)

x=int(input('Enter x:'))
n=int(input('Enter n:'))
print('Series 1:',ser(x,n))
print('Series 2:',ser1(x,n))
