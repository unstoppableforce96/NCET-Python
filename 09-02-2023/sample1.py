f = open("def.txt", "w")
n = int(input())
for i in range(n):
    s = input()
    f.write(s + '\n')
f.close()