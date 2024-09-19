import mysql.connector as m 
a = m.connect(
	host = "localhost",
	user = "root",
	password = "root",
                database='record'
)
cur=a.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS STUDENT (ROLL INT PRIMARY KEY,NAME VARCHAR(30),TOTAL INT, COURSE VARCHAR(30) CHECK (COURSE IN ("CS","BIOLOGY","COMMERCE","EG")),DOB DATE);')
cur.execute('INSERT INTO STUDENT VALUES(1,"RAM",150,"CS","2007-02-24"),(2,"SHAM",150,"EG","2003-05-22"),(3,"SAM",420,"BIOLOGY","2008-02-20"),(4,"RAMAN",390,"COMMERCE","2007-10-27"),(5,"MOHAN",493,"CS","2008-02-18");')
print('Maximum total marks, minimum total marks and number of students in each course where there at least 2 students')
cur.execute('SELECT MAX(TOTAL),MIN(TOTAL),COUNT(TOTAL),COURSE FROM STUDENT GROUP BY COURSE HAVING COUNT(TOTAL)=2;')
for x in cur:
    print(x[3],'\nMaximum Total :',x[0],'\nMinimum Total :',x[1])
print('\nDetails ofstudents born in the month of May 2003 who have scored total between 100 to 200')
cur.execute('SELECT * FROM STUDENT WHERE MONTH(DOB)="05" AND 100<=TOTAL<=200 AND YEAR(DOB)="2003";')
for x in cur:
    print(x[0],x[1],x[2],x[3],x[4],sep='\t')
print('\nStudent list in the descending order of total')
cur.execute('SELECT * FROM STUDENT ORDER BY TOTAL DESC;')
for x in cur:
    print(x[0],x[1],x[2],x[3],x[4],sep='\t')
print('\nIncrease total marks for CS students by 5 %, for those, whose total is less than 180')
cur.execute('UPDATE STUDENT SET TOTAL=TOTAL+(TOTAL*0.05) WHERE COURSE="CS" AND TOTAL<180;')
cur.execute('SELECT * FROM STUDENT;')
for x in cur:
    print(x[0],x[1],x[2],x[3],x[4],sep='\t')
a.commit()
