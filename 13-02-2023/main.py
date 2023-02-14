import os # import module os

##os.getcwd() --> getcurrentworkingdirectory
##path = os.getcwd()
##print(f"Your file exists at {path}")

# os.chdir() -->
##os.chdir("D:\\NCET\\Python - TtT\\Temp")
##print(f'The directory after chdir is {os.getcwd()}')
##f = open("test1.txt", "w")
##f.write("this file is created using os module")
##f.close()

##os.mkdir() --> make directory
##os.mkdir("testdir")
##os.chdir("testdir")
##f = open("file1.txt", "w")
##f.close()

##num_of_folders = int(input())
##for _ in range(num_of_folders):
##    dr = input() # read a string
##    os.mkdir(dr)


##os.mkdir("Z/Y/X/W")



##os.mkdir("A")

# os.makedirs("A/B/C/D")
# create directories B inside A, C inside B...

##os.makedirs("Z/W/Y/X")
#os.rmdir() --> remove a folder, if the folder is empty
##os.rmdir("A") # removes A
##print("A is removed")
##os.rmdir("B")
##print("B is removed")

##os.remove("B")

##os.removedirs("Z/W/Y/X")
##print(os.getcwd())


# os.path --> os.path.isdir() --> whether it's a directory or not
# os.path --> os.path.isfile() --> whether the given path is file not
#print(os.path.isdir("D:\\NCET\\Python - TtT\\OsModule\\testdir"))
##if os.path.isdir("testdir"):
##    pass
##else:
##    os.mkdir("testdir")
##
##print("hello this one will be printed")
##print("Hello this one will also be printed")


# if os.path.isfile(path) --> True, if the path leads to a file, Fasle otherwise
##print(os.path.isfile(os.getcwd()))
file = "thisisfile.txt"
path = os.getcwd()
x = os.path.join(path, file)
print(x)
# os.path.extsplit()








