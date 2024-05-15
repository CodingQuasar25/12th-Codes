d={}
def add():
    t=int(input('Enter Telephone Number to Add : '))
    d[t]=input('Enter Name to Add : ')
def disp():
    for i in d:
        print(i,':',d[i])
def modi(n,e):
    d[n]=e
def dele(n):
    d.pop(n)
while True:
    n=int(input('1.Add\n2.View\n3.Modify\n4.Delete\n5.Exit\nEnter Choice : '))
    if n==1:
        add()
    elif n==2:
        disp()
    elif n==3:
        n=int(input('Enter Telephone Number to Change : '))
        e=input('Enter Name to change : ')
        modi(n,e)
    elif n==4:
        n=int(input('Enter Telephone Number to Delete : '))
        dele(n)
    elif n==5:
        break
    
