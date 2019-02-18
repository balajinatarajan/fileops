import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="media"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT filename, filesize FROM mediaindex WHERE filetype=\"Video\"")
result = mycursor.fetchall()
index = 0
for x in result:
    index = index + 1
    if(index % 1000 == 0):
      print(index)
    filesize = x[1]
    filename = x[0]
    if(len(filename.split('.')) == 2):
        filenamelike = "%" + filename.split('.')[0] + "%"
        mycursor.execute("""SELECT filename, filesize FROM mediaindex WHERE filetype = 'Video' and filename like \"%s\"""" % (filenamelike))
        dupresult = mycursor.fetchall()
        for y in dupresult:
            if(y[0] != filename and y[1] == filesize):
                mycursor.execute("""INSERT INTO dupevideo (filename) VALUES (\"%s\")""" % (y[0]))
                mydb.commit()