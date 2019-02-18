import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="media"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT filename, filetype, filesize, filehash  FROM mediaindex WHERE filetype=\"Image\"")
result = mycursor.fetchall()
index = 0
for x in result:
    index = index + 1
    if(index % 1000 == 0):
      print(index)
    filehash = x[3]
    filesize = x[2]
    filename = x[0]
    mycursor.execute("""SELECT filename, filesize FROM mediaindex WHERE filehash = '%s'""" % filehash)
    dupresult = mycursor.fetchall()
    filename_to_keep = filename
    for y in dupresult:
      if(y[1] >= filesize):
        filename_to_keep = y[0]
    mycursor.execute("""SELECT count(*) FROM goldenmedialist WHERE filehash = '%s'""" % filehash)
    count = mycursor.fetchone()
    if(count[0] == 0):
      mycursor.execute("""INSERT INTO goldenmedialist (filename,filehash) VALUES (\"%s\",\"%s\")""" % (filename_to_keep,filehash))
      mydb.commit()