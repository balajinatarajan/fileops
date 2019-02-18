import mysql.connector
import os
import shutil

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="media"
)

mycursor = mydb.cursor()

mycursor.execute("select filename from mediaindex where filename like \"%.AAE%\" and filetype = \"Unknown\"")
result = mycursor.fetchall()

for x in result:
    filename = x[0]
    try:
      os.remove(filename)    
      print(filename)
    except:
      print('ignore')
    