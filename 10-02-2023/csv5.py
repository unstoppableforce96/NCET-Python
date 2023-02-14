import csv
f = open("xyz.csv", "w", newline='') # 
# csvwriterobject
c = csv.writer(f) # creation of csvwriter
fields = ['S.No', 'Name', 'Age']
record1 = ['1', 'Pavan', '26']
record2 = ['2', 'Rajesh', '30']
record3 = ['3', 'Kiran', '31']
data = [fields, record1, record2, record3]
c.writerows(data)
f.close()