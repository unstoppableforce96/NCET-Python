import csv
f = open("data.csv", "r+")
# csvreader
c = csv.reader(f) # csvreaderobject
data = list(c)
for line in data:
    for field in line:
        print(field, "\t", end='')
    print()