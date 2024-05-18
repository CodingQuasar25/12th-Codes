def palindrome(x):
    n,c=x,0
    while n>0:
        c=(n%10)+c*10
        n//=10
    if c==x:
        return 1
    else:
        return -1
def specialnumber(x):
    n,c=x,0
    while n>0:
        k=1
        for i in range(1,n%10+1):
            k*=i
        c+=k
        n//=10
    if c==x:
        return 1
    else:
        return -1
