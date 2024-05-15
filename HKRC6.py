def allvowel(x):
    c=0
    print ('The words with all vowels -',end=' ')
    for i in x:
        if 'a'and'e'and'i'and'o'and 'u' in i:
            print(i,end=' ')
            c+=1
        else :
            continue
    if c==0:
        print('NIL')
    print()    
    
def bmi(x):
    for i in range(len(x)):
        l=x[i][1]/x[i][0]**2
        if l>30:
            print('Person',i+1,'Obese',l)
        elif 25<=l<=30:
            print('Person',i+1,'Overweight',l)
        elif 18.5<=l<=25:
            print('Person',i+1,'Normal',l)
        elif l<18.5:
            print('Person',i+1,'Underweight',l)
        
while True:
    n=int(input('1.Display words with all vowels present in it\n2.BMI\n3.Exit\nEnter Choice:'))
    if n==1:
        t=()
        p=int(input('Enter number of people:'))
        for i in range(p):
            l=input('Enter Element:')
            t+=l,
        allvowel(t)
    elif n==2:
        t=()
        p=int(input('Enter number of elements:'))
        for i in range(1,p+1):
            print('For Person',i)
            l=int(input('Enter Height in metres:'))
            w=int(input('Enter Weight in kilograms:'))
            t+=(l,w,),
        bmi(t)
    elif n==3:
        break
    
