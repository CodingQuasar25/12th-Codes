def mean(x):
    c=0
    for i in x:
        c+=i
    print('Mean is',c/len(x))
def mode(x):
    l,e={},0
    for i in x:
        c=0
        for j in x:
            if i==j:
                c+=1
        l[i]=c
    for i in l:
        if l[i]>e:
            e=l[i]
    print('The mode is',end=' ')
    for k in l:
        if l[k]==e:
            print(k,end=' ')
    print()
def median(x):
    n=x
    def bubble(n):
        for i in range (len(n)-1):
            for j in range (len(n)-i-1):
                if n[j]>n[j+1]:
                    n[j],n[j+1]=n[j+1],n[j]
    bubble(n)
    if len(n)%2==0:
        print('Median is',(n[len(n)//2-1]+n[(len(n)//2)])/2)
    else:
        print('Median is',n[len(n)//2])

n=int(input('Enter number of terms:'))
x=[]
for i in range(n):
    n1=int(input('Enter nos:'))
    x.append(n1)
while True:
    n=int(input('1.Mean\n2.Mode\n3.Median\n4.Exit\nEnter Choice:'))
    if n==1:
        mean(x)
    elif n==2:
        mode(x)
    elif n==3:
        median(x)
    elif n==4:
        break
    
