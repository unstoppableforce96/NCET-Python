f = open("abc.txt", "w")
f.write("This is write mode")
f.close()

f = open("abc.txt", "r")
data = f.read(7)
print(data)