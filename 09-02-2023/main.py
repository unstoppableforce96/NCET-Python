f = open("abc.txt", "w")
# print(f.writable())
f.write('Pavan\n') # We can write a string to the file
f.write('Rajesh\n')
f.write('Kiran\n')
f.close()
# abc.txt --> PavanRajeshKiran