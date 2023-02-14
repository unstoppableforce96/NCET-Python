import csv
f = open("data.csv", "r")
# csvreader
c = csv.reader(f) # csvreaderobject
data = list(c)
print(data)