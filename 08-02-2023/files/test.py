f = open("abc.txt", "r")
print("Name of the file: ", f.name)
print("Mode of the file: ", f.mode)
print("Is readable?: ", f.readable())
print("Is writable?: ", f.writable())
print("Is the file closed?: ", f.closed)
f.close()
print("Is the file closed?: ", f.closed)
# what is the name of the file f.name
# in which mode the file is opened f.mode
# is the file readable f.readable()
# is the file writable f.writable()
# whether the file is closed or not f.closed