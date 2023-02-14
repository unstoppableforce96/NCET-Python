import csv
f = open("newcsv.csv", "w", newline='') # 
# csvwriterobject
c = csv.writer(f) # creation of csvwriter
fields = ['S.No', 'Name', 'Age']
record1 = ['1', 'Pavan', '26']
c.writerow(fields)
c.writerow(record1)
f.close()