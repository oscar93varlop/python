import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="admin", password="es:pgCmOCjL.!&8CzM", port=3306)

mycursor = mydb.cursor()

mycursor.execute("show databases")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
