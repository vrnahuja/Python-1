import mysql.connector
mydb=mysql.connector.connect(
        user='root',
        passwd='',
        host='localhost',
        database="python")
db=mydb.cursor()
db.execute("select * from data")
print("DATA:")
r=db.fetchall()
for i in r: 
    print(i)