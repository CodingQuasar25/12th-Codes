def bsearch(a,b):
    a=sorted(a)
    h=len(a)-1
    l=0
    while h>=l:
        mid=(h+l)//2
        if a[mid]==b:
            return mid
            break
        if a[mid]>b:
            h=mid-1
        if a[mid]<b:
            l=mid+1
def revstr(a):
    b=''
    for i in a:
        b=i+b
    return b
while True:
    opt=int(input('1.Binary Search\n2.Reverse a string\n3.Exit\nEnter Choice:'))
    if opt==1:
        n=eval(input('Enter list of numbers:'))
        e=int(input('Enter element to search:'))
        print('The index of',e,'is',bsearch(n,e))
    elif opt==2:
        n=input('Enter string to reverse:')
        print(revstr(n))
    elif opt==3:
        break
