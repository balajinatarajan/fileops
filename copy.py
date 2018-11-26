import os
import shutil

def iterate_dir_and_copy_files_recursively(srcdir, dest):
    src_files = os.listdir(srcdir)
    for file_name in src_files:
        full_file_name = os.path.join(srcdir, file_name)
        if (os.path.isdir(full_file_name)):
            iterate_dir_and_copy_files_recursively(full_file_name,dest)
        else:
            if ".JPG" in file_name or ".jpg" in file_name or ".jpeg" in file_name or ".JPEG" in file_name or ".png" in file_name or ".PNG" in file_name or ".mp4" in file_name or ".MP4" in file_name or ".mov" in file_name or ".MOV" in file_name  or ".m4v" in file_name  or ".M4V" in file_name:
                shutil.copy(full_file_name, dest)    

src = "/Volumes/BILLU/tmp"
dest = "/Volumes/BILLU/ALL_MEDIA"
#iterate_dir_and_copy_files_recursively(src, dest)