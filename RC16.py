def emt(l):
    if len(l)==0:
        return False
    else:
        return True
def push(l):
    cn=input('Enter Country Name : ')
    ca=input('Enter Capital : ')
    l.append([cn,ca])
def Pop(l):
    if emt(l):
        l.pop()
    else:
        print('Stack Underflow')
def disp(l):
    if emt(l):
        print('The Stack :')
        for i in range (-1,-(len(l)+1),-1):
            print(l[i][0],':',l[i][1])
    else:
        print('Stack Underflow')
def peek(l):
    if emt(l):
        print('The Peek Element is',l[-1][0],':',l[-1][1])
    else:
        print('Stack Underflow')
l=[]
while True:
    op=int(input('Menu\n1.Insert\n2.Delete\n3.Display Stack\n4.Peek\n5.Exit\nEnter Choice : '))
    if op==1:
        push(l)
    elif op==2:
        Pop(l)
    elif op==3:
        disp(l)
    elif op==4:
        peek(l)
    elif op==5:
        break
    else:
        print('Incorrect Choice')
