import csv
f = open("data.csv", "r")
# csvreader
c = csv.reader(f) # csvreaderobject
data = list(c)
print(data)
data[2][2] = '31'
for line in data:
    for field in line:
        print(field, "\t", end='')
    print()