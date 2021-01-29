
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_PASS = "postgres"
DB_USER = "postgres"



import psycopg2



conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor()
msg = "hello python"
print(msg)
postgreSQL_select_Query = "delete from student"
cur.execute(postgreSQL_select_Query)
with open(r'C:\Users\saurabhc\Desktop\postgres.txt', 'r') as f:
    next(f)
    cur.copy_from(f, 'student', sep=',')

conn.commit()

postgreSQL_select_Query = "select * from student"
cur.execute(postgreSQL_select_Query)
print("Selecting rows from student table")
student = cur.fetchall() 
   
print("Print Student Details:")
for row in student:
   print("Rollno = ", row[0], )
   print("Student name = ", row[1])
   print("Student age = ", row[2])
   print("Student class = ", row[3])
   print("Student Year = ", row[4])
   print("Student Date of birth  = ", row[5], "\n")

cur.close()
conn.close()