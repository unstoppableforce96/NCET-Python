# A directory with the name File_Management
import os
import shutil

list_extensions = []
# os.mkdir("File_Management")
for file in os.listdir():
    if os.path.isfile(file) == True:
        list_extensions.append(file.split('.')[-1])
# print(list_extensions)
list_extensions = list(set(list_extensions))
list_extensions.remove('py')

# print(list_extensions)
for ex in list_extensions:
    os.mkdir("File_Management" + '/' + ex)
    for file in os.listdir():
        if os.path.isfile(file) == True:
            if file.split('.')[-1] == ex:
                shutil.move(file, 'File_Management' + '/' + ex)