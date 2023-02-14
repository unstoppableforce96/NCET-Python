f = open("xyz.txt", "r")
# read(), readline(), readlines()
s = f.read() # return a string which contains the entire data in the file
print(s)
print(len(s))
# print(type(s))
f.close()