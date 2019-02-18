import os
import shutil
from pprint import pprint
import imagehash
from PIL import Image, ExifTags
from termcolor import cprint
import mysql.connector

def hash_file(file):
    try:
        hashes = []
        img = Image.open(file)
        # hash the image 4 times and rotate it by 90 degrees each time
        for angle in [ 0, 90, 180, 270 ]:
            if angle > 0:
                turned_img = img.rotate(angle, expand=True)
            else:
                turned_img = img
            hashes.append(str(imagehash.phash(turned_img)))
        hashes = ''.join(sorted(hashes))
        #cprint("\tHashed {}".format(file), "blue")
        return hashes
    except OSError:
        cprint("\tUnable to open {}".format(file), "red")
        return None

def get_file_size(file_name):
    try:
        return os.path.getsize(file_name)
    except FileNotFoundError:
        return 0

def insert(mydb, filename, filetype, filesize, filehash):
    mycursor = mydb.cursor()
    sql = "INSERT INTO mediaindex (filename, filetype, filesize, filehash) VALUES (%s, %s, %s, %s)"
    val = (filename, filetype, int(filesize), filehash)
    mycursor.execute(sql, val)


mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  passwd="root",
  database="media"
)

srcdir = "/Volumes/BILLU/ALL_MEDIA"
src_files = os.listdir(srcdir)
for filename in src_files:
    filename = os.path.join(srcdir, filename)
    if ".JPG" in filename or ".jpg" in filename or ".jpeg" in filename or ".JPEG" in filename or ".png" in filename or ".PNG" in filename:
        filetype = "Image"
        filesize = get_file_size(filename)
        filehash = hash_file(filename)
        insert(mydb, filename, filetype, filesize, filehash)
    elif ".mp4" in filename or ".MP4" in filename or ".mov" in filename or ".MOV" in filename  or ".m4v" in filename  or ".M4V" in filename:
        filetype = "Video"
        filesize = get_file_size(filename)
        filehash = "NA"
        insert(mydb, filename, filetype, filesize, filehash)  
    else:
        filetype = "Unknown"
        filesize = get_file_size(filename)
        filehash = "NA"
        insert(mydb, filename, filetype, filesize, filehash)  
    mydb.commit()