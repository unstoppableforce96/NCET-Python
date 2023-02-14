f = open("input.txt", "r")
s = f.read()
lst = list(map(int, s.split()))
x = open("output.txt", "w")
for i in lst:
    x.write(str(i * i) + '\n')
f.close()
x.close()