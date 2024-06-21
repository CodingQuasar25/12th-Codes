def name():
    f=open('abc.txt','w')
    n=int(input('Enter number of lines: '))
    for i in range (1,n+1):
        st=input('Enter text: ')
        f.write(st+'\n')
    f.close()
def openname() :
    f=open('abc.txt','r')
    m=f.read().split('\n')
    for i in m :
        print(i)
    f.close()
def countline():
    with open ('abc.txt','r') as f:
        print('Number of Lines: ',len(f.readlines()))
def letu():
    with open ('abc.txt','r') as f, open ('copy.txt','w') as w:
        s=f.readlines()
        for i in s:
            for j in i.split():
                if 'u' in j.lower():
                    w.write(j+' ')
    with open ('copy.txt','r') as w:
        s=w.readlines()
        for i in s:
            print(i)
def togcas():
    with open ('abc.txt','r') as f,open ('temp.txt','w') as w:
        s=f.read(1)
        while s:
                    if s.islower():
                        w.write(s.upper())
                    elif s.isupper():
                        w.write(s.lower())
                    else:
                        w.write(s)
                    s=f.read(1)
    import os
    os.remove('abc.txt')
    os.replace('temp.txt','abc.txt')
    with open ('abc.txt','r') as w:
        s=w.readlines()
        for i in s:
            print(i,end='')
while True :
    n=int(input('Menu Driven Code:\n1.Create a File\n2.Display\n3.Display Count Lines\n4.Copy all words with U/u\n5.Toggle Case\n6.Exit\nEnter Choice:'))
    if n==1:
        name()
    elif n==2:
        openname()
    elif n==3:
        countline()
        print()
    elif n==4:
        print('The copied file is')
        letu()
        print()
    elif n==5:
        print('The toggled case is')
        togcas()
        print()
    elif n==6:
        break
    else:
        print('You have entered the wrong choice')
        
