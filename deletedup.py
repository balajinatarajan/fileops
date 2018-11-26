import os
import shutil

srcdir = "/Volumes/BILLU/ALL_MEDIA"

src_files = os.listdir(srcdir)
for file_name in src_files:
    full_file_name = os.path.join(srcdir, file_name)
    if "(1)" in file_name:
        os.remove(full_file_name)    