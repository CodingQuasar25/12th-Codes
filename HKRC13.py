import pickle
def create():
    try:
        with open ('Employee.dat','wb') as f:
            n=int(input('Enter number of Employees : '))
            for i in range (1,n+1):
                n1={}
                print('For Employee',i,':')
                n1['Name']=input('Enter Name : ')
                n1['Age']=int(input('Enter Age : '))
                n1['Department']=input('Enter Department : ')
                n1['Designation']=input('Enter Designation : ')
                n1['Salary']=int(input('Enter Salary : '))
                pickle.dump(n1,f)
    except Exception :
        print('UnknownError')
def disp():
    try:
        with open ('Employee.dat','rb') as f:
            i=pickle.load(f)
            while True:
                if i['Department'].lower()=='admin' and i['Salary']>50000 and i['Designation'].lower()=='manager':
                    print('Name : ',i['Name'],',','Age : ',i['Age'],',','Department : ',i['Department'],',','Designation : ',i['Designation'],',','Salary : ',i['Salary'])
                elif i['Department'].lower()=='finance' and i['Salary']>50000 and i['Designation'].lower()=='manager':
                    print('Name : ',i['Name'],',','Age : ',i['Age'],',','Department : ',i['Department'],',','Designation : ',i['Designation'],',','Salary : ',i['Salary'])
                try:
                    i=pickle.load(f)
                except EOFError :
                    break
    except Exception :
        print('UnknownError')

def delete():
    try:
        with open ('Employee.dat','rb') as f , open ('Temp.dat','wb') as t:
            i=pickle.load(f)
            while i:
                if i['Age']<=58:
                   pickle.dump(i,t)
                try:    
                    i=pickle.load(f)
                except EOFError :
                    break
        import os
        os.remove('Employee.dat')
        os.rename('Temp.dat','Employee.dat')
        print('The Final File:')
        with open ('Employee.dat','rb') as f :
            i=pickle.load(f)
            while i:
                print('Name : ',i['Name'],',','Age : ',i['Age'],',','Department : ',i['Department'],',','Designation : ',i['Designation'],',','Salary : ',i['Salary'])
                try:    
                    i=pickle.load(f)
                except EOFError :
                    break
    except Exception :
        print('UnknownError')
while True:
    n=int(input('''Menu\n1.Create File\n2.Display details of Managers earning more than 50000 in Finance and in Admin Dept.\n3.Delete the employee details who have reached retirement age(58 years)\n4.Exit\nEnter Choice : '''))
    if n==1:
        create()
    elif n==2:
        disp()
    elif n==3:
        delete()
    elif n==4:
        break
    else:
        print('Wrong Choice')
          
            
                  
                    
