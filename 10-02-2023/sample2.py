f = open("abc.txt", "w+") # write as well as read
f.write("This is write mode")
f.seek(7, 0)
data = f.read(7)
print(data)
f.close()
