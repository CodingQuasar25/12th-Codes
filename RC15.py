def emt(l):
    if len(l)==0:
        return False
    else:
        return True
def push(l):
    l.append(int(input('Enter Value to Push : ')))
def Pop(l):
    if emt(l):
        l.pop()
    else:
        print('Stack Underflow')
def disp(l):
    if emt(l):
        print('The Stack :')
        for i in range (-1,-(len(l)+1),-1):
            print(l[i])
    else:
        print('Stack Underflow')
def peek(l):
    if emt(l):
        print('The Peek Value is',l[-1])
    else:
        print('Stack Underflow')
l=[]
while True:
    op=int(input('Menu\n1.Push\n2.Pop\n3.Display Stack\n4.Peek\n5.Exit\nEnter Choice : '))
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
