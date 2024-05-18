#Save the number.py file in your PC and then Run this Code
import number as n

while True:
    op=int(input('1.Palindrome Check\n2.Special Number Check\n3.Exit\nEnter Choice:'))
    if op==1:
        n1=int(input('Enter Number of Elements in the Tuple:'))
        m,c=(),0
        for i in range(1,n1+1):
            print('Enter Element',i,':',end='')
            t=int(input())
            m+=t,
            if n.palindrome(t)==1:
                c+=1
        if c>0:
            print('The Palindrome Numbers are ',end='')
            for i in m:
                if n.palindrome(i)==1:
                    print(i,end=', ')
        else:
            print('There are no Palindrome Numbers')
        print()
    elif op==2:
        l=int(input('Enter Lower Limit: '))
        u=int(input('Enter Upper Limit: '))
        c=0
        for i in range (l,u+1):
            if n.specialnumber(i)==1:
                c+=1    
        if c>0:
            print('The Special Numbers are ',end='')
            for i in range (l,u+1):
                if n.specialnumber(i)==1:
                    print(i,end=', ')
        else:
            print('There are no Special Numbers')
        print()
