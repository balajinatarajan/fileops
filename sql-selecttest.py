import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="media"
)

mycursor = mydb.cursor()
filehash = '866fe01bf20ff026aa956be55438d1aad3c5b5a1a7a5a18cff3fbe4f01928801'
mycursor.execute("""SELECT count(*) FROM mediaindex WHERE filehash = '%s'""" % filehash)
count = mycursor.fetchone()
print(count[0])