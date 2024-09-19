import mysql.connector as m
a = m.connect(
	host = "localhost",
	user = "root",
	password = "root",
                database='record'
)
cr=a.cursor()
cr.execute('CREATE TABLE IF NOT EXISTS EMPLOYEE1 (EMPNO INT PRIMARY KEY,NAME VARCHAR(25),DESIG VARCHAR(25),DEPNO INT,SALARY INT);')
cr.execute('CREATE TABLE IF NOT EXISTS DEPARTMENT1 (DEPTNO INT PRIMARY KEY,DNAME VARCHAR(25),LOCATION VARCHAR(25));')
cr.execute('INSERT INTO EMPLOYEE1 VALUES (120,"RAM","MANAGER",2,500000),(123,"RAMAN","OFFICER",2,200000),(210,"MOHAN","MANAGER",3,550000),(157,"SAM","CLERK",4,50000),(143,"KUMAR","MANAGER",1,550000);')
cr.execute('INSERT INTO DEPARTMENT1 VALUES (1,"RESEARCH AND DEVELOPMENT","CHENNAI"),(2,"ADMIN","DELHI"),(3,"MARKETING","MUMBAI"),(4,"FINANCE","KOLKATA");')
print('DETAILS OF MANAGERS:')
cr.execute('SELECT Empno, Name, Desig, Deptno, Salary,Dname, Location FROM EMPLOYEE1,DEPARTMENT1 WHERE DESIG="MANAGER" AND DEPNO=DEPTNO;')
for i in cr:
    for j in i:
        print(j,end='\t')
    print()
a.commit()
