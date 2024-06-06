def name():
    f=open('abc.txt','w')
    n=int(input('Enter n: '))
    for i in range (n):
        st=input('Enter the word: ')
        f.write(st+' ')
    f.close()
def openname() :
    f=open('abc.txt','r')
    m=f.read().split()
    for i in m :
        print(i)
    f.close()
def addmore() :
    f=open('abc.txt','a')
    for i in range (3):
        n=input('Enter Name: ')
        f.write(n+' ')
    f.close()
    openname()
def space():
    f=open('abc.txt','r')
    print('Count of spaces : ',len(f.read().split())-1)
    f.close()
def the():
    f=open('abc.txt','r')
    m,c=f.read().split(),0
    for i in m:
        if i.lower()=='the':
            c+=1
    print('Count of "the" : ',c)
    f.close()
def vowel():
    f=open('abc.txt','r')
    m,c=f.read(),0
    for i in m:
        if i.lower() in 'aeiou':
            c+=1
    print('Count of vowels : ',c)
    f.close()
def openname2() :
    f=open('cba.txt','r')
    m=f.read().split()
    for i in m :
        print(i)
    f.close()
def copyfile():
    f=open('abc.txt','r')
    m=f.read()
    f.close()
    f1=open('cba.txt','w')
    f1.write(m)
    f1.close
    

name()
openname()
addmore()
space()
the()
vowel()
copyfile()
openname2()
