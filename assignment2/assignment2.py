# Task 2: Read a CSV File 
import csv 
import os
def read_employees():
    dict1 = {}
    list1 = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader =csv.reader(file)
            first = True
            for row in reader:
                if first:
                    dict1["fields"] = row
                    first = False
                else:
                    list1.append(row)
            dict1["rows"] = list1
    except Exception as e:
        print("Error in syntax of code")

    return dict1
employees = read_employees()

# Task 3: Find the Column Index 
def column_index(employee_id):
    return employees["fields"].index(employee_id)

employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    col = column_index("first_name")
    row= employees["rows"][row_number]
    return row[col]

# Taske 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    col= column_index("last_name")
    employees["rows"].sort(key = lambda row: row[col])
    return employees["rows"]
sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    result = {}
    fields = employees["fields"]
    for i in range(1, len(fields)):
        result[fields[i]]= row[i]
    return result 
print(employee_dict(employees["rows"][0]))

# Task 9: A dict of dicts, for all Employees 
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        result[row[employee_id_column]] = employee_dict(row)
    return result
print(all_employees_dict())

# Task 10: use the os Module
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11: Creating Your Own Module
import custom_module 
def set_that_secret(new):
    custom_module.set_secret(new)

set_that_secret("This99")
print(custom_module.secret)

# Task 12: read minutes1.csv and minutes2.csv
def csv_read(path):
    result = {}
    rows = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        first = True
        for row in reader:
            if first:
                result["fields"] = row
                first=False
            else:
                rows.append(tuple(row))
    result ["rows"] = rows
    return result 


def read_minutes():
    minutes1= csv_read("../csv/minutes1.csv")
    minutes2= csv_read("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    min1 = set(minutes1["rows"])
    min2 = set(minutes2["rows"])
    return min1.union(min2)
minutes_set = create_minutes_set()

# Task 14
from datetime import datetime

def create_minutes_list():
    list1 = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list1))
minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x:x[1])
    changed = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(changed)

    return changed 
write_sorted_list()