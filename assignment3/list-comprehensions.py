import csv 

with open("../csv/employees.csv", newline= "") as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

header= rows[0]
first = header.index("first_name")
last = header.index("last_name")

names = [row[first]+ " " + row[last] for row in rows[1:]]
print(names)

name_e = [name for name in names if "e" in name]
print(name_e)