import csv
def finalprice():
    with open ('items.csv','r') as s:
        b=csv.reader(s)
        c=[]
        for i in b:
            with open ('gst.csv','r') as f:
                a=csv.reader(f)
                for j in a:
                    if i[2].lower()==j[0].lower():
                        d=str(int(i[3])+((int(j[1])/100)*int(i[3])))
                        c.append([i[0],i[1],i[2],i[3],d])
    with open ('items.csv','w',newline='') as f:
        a=csv.writer(f)
        a.writerows(c)
    with open ('items.csv','r') as f:
        a=csv.reader(f)
        for i in a:
            print('Item ID : ',i[0],' , Name : ',i[1],' , Category : ',i[2],' , Unit Price : ',i[3],' , Final Price : ',i[4],sep='')

def create1():
    with open ('gst.csv','w',newline='') as f,open ('items.csv','w',newline='') as s:
        a,b,c=csv.writer(f),csv.writer(s),[]
        n=int(input('Enter Number of Items : '))
        for i in range(1,n+1):
            print('Item Number',i)
            itid=int(input('Enter Item ID : '))
            na=input('Enter Name : ')
            ca=input('Enter Category : ')
            un=int(input('Enter Unitprice : '))
            c.append([itid,na,ca,un,' '])
        b.writerows(c)
        a.writerows([['Automobiles','25'],['Stationary','12'],['Chocolates','10'],['Dairy','3']])
    finalprice()
create1()

            
            
        
