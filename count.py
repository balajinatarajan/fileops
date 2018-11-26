import os
import shutil

filetypes = []

def iterate_dir_and_count_files_recursively(srcdir, count):
    global filetypes
    src_files = os.listdir(srcdir)
    for file_name in src_files:
        full_file_name = os.path.join(srcdir, file_name)
        if (os.path.isdir(full_file_name)):
            count = iterate_dir_and_count_files_recursively(full_file_name, count)
        else:
            if ".JPG" in file_name or ".jpg" in file_name or ".jpeg" in file_name or ".JPEG" in file_name or ".png" in file_name or ".PNG" in file_name or ".mp4" in file_name or ".MP4" in file_name or ".mov" in file_name or ".MOV" in file_name  or ".m4v" in file_name  or ".M4V" in file_name:
                count = count + 1
            extn = ""
            try:
                extn = file_name.rsplit(".",1)[1]
            except:
                pass
            if extn not in filetypes:
                filetypes.append(extn)
    return count
                
src = "/Volumes/MONTUX-2TB"
count = iterate_dir_and_count_files_recursively(src, 0)
print "Total media: %s" % (count)
print (filetypes)