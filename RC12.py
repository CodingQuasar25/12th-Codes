import pickle
def create():
    try:
        with open ('Student.dat','wb') as f:
            n1=[]
            n=int(input('Enter number of students : '))
            for i in range (1,n+1):
                print('For student',i,':')
                rn=int(input('Enter roll name : '))
                na=input('Enter name : ')
                st=input('Enter stream : ')
                t=int(input('Enter total : '))
                n1.append([rn,na,st,t])
            pickle.dump(n1,f)
    except Exception :
        print('UnknownError')
def topper():
    try:
        with open ('Student.dat','rb') as f:
            li={}
            l=pickle.load(f)
            for i in l:
                    if i[2].upper() not in li :
                        li[i[2].upper()]=i[3]
                    elif i[2].upper() in li and i[3]>li[i[2].upper()]:
                        li[i[2].upper()]=i[3]
            for i in l:
                for j in li:
                    if i[2].upper()==j and i[3]==li[j]:
                        print('Stream : ',i[2].title())
                        print('Roll Number : ',i[0],'\n','Name : ',i[1],'\n','Stream : ',i[2],'\n','Total Mark : ',i[3],'\n',sep='')
    except Exception :
        print('UnknownError')
def change():
    try:
        with open ('Student.dat','rb') as f:
            l=pickle.load(f)
            for i in l:
                if i[2].upper()=='BIOLOGY' :
                    i[3]+=3
                if i[2].upper()=='EG' or i[2].upper()=='ENGINEERING GRAPHICS':
                    i[3]-=2
            for i in l:
                print('Roll Number : ',i[0],'\n','Name : ',i[1],'\n','Stream : ',i[2],'\n','Total Mark : ',i[3],'\n',sep='')
    except Exception :
        print('UnknownError')
while True:
    n=int(input('Menu\n1.Create File\n2.Display Stream wise topper details\n3.Increment the total by 3 marks for students in the biology stream and decrement by 2 for students in EG stream.\n4.Exit\nEnter Choice : '))
    if n==1:
        create()
    elif n==2:
        topper()
    elif n==3:
        change()
    elif n==4:
        break
    else:
        print('Wrong Choice')
          
            
                  
                    
