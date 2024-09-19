import mysql.connector as m
import csv as c
a = m.connect(
	host = "localhost",
	user = "root",
	password = "root",
                database='record'
)
cur=a.cursor()
with open ('Student.csv','w',newline="") as f:
    b=c.writer(f)
    cur.execute('desc student;')
    ad=[]
    for i in cur:
        ad.append(i[0])
    b.writerow(ad)
    cur.execute('Select * from student ;')
    for i in cur:
        b.writerow(i)
with open ('Student.csv','r') as f: 
    m=c.reader(f)
    for i in m:
        for j in i:
                print(j,end=',\t')
        print()
with open ('Student.csv','r') as f: 
    m,k=c.reader(f),[]
    for i in m:
        k.append(i)
    m,n=k[1:],k[0]
    q,l,o=0,[],0
    for i in range(len(m)):
        if int(m[i][2])>q:
            o,q=i,int(m[i][2])
    for i in range(len(m)):      
        if int(m[i][2])==q:
            l.append(m[i])
    print('Top Scorers:')
    l=[n]+l
    for i in l:
        for j in i:
                print(j,end=',\t')
        print()
