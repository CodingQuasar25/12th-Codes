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
def stenword ():
    with open ('abc.txt','r') as f:
        c=f.readline()
        ct=0
        while (c):
            c=c.split()
            for i in c:
                if i[0].lower() in 'aeiou' and i[-1].lower() in 'aeiou':
                    print(i)
                    ct+=1
            c=f.readline()
        if ct==0:
                print('None')
def count():
    with open ('abc.txt','r') as f:
        c=0
        s=f.readlines()
        for i in s:
            c+=len(i.split())
        print('Total number of words in the file: ',c)
def palin():
    with open ('abc.txt','r') as f:
        c=f.readline()
        ct=0
        while (c):
            c=c.split()
            for i in c:
                if i.lower()==i[::-1].lower() and len(i)!=1:
                    print(i)
                    ct+=1
            c=f.readline()
        if ct==0:
                print('None')
while True :
    n=int(input('Menu Driven Code:\n1.Create a File\n2.Display\n3.Display Count of Words\n4.Display the words that are palindrome\n5.Display words that start and end with a vowel\n6.Exit\nEnter Choice:'))
    if n==1:
        name()
    elif n==2:
        openname()
    elif n==3:
        count()
        print()
    elif n==4:
        print('The palindrome words are :')
        palin()
        print()
    elif n==5:
        print('The words that start and end with a vowel :')
        stenword()
        print()
    elif n==6:
        break
    else:
        print('You have entered the wrong choice')
