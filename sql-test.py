import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="media"
)

mycursor = mydb.cursor()

sql = "INSERT INTO mediaindex (filename, filetype, filesize, filehash) VALUES (%s, %s, %s, %s)"
val = ("John.jpg", "Image", 236509, "9fecc1cc3f26c308a722195d8c809bffda46946e6e8c96a6f28d4c77c9228e55")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")