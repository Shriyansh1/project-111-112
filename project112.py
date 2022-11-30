import os   
import shutil

from_dir = "D:/"
to_dir = "E:/"

list_of_file = os.listdir(from_dir)
#print(list_of_file)

for xy in list_of_file:
    name,ext = os.path.splitext(xy)
    #print(name,ext)

    if ext == '':
        continue

    if ext in ['.txt','.pdf','.docx','.doc']:

        path1=from_dir+'/'+xy
        path2=to_dir+'/'+"download"
        path3=to_dir+'/'+"download"+'/'+xy

        if os.path.exists(path2):
            shutil.move(path1,path3)

        else: 
            os.makedirs(path2)
            shutil.move(path1,path3)