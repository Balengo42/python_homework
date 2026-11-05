# Task 1:
import pandas as pd
task1_data_frame =pd.DataFrame({
    "Name":['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']})


task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000,80000,90000]


task1_older = task1_with_salary.copy()
task1_older["Age"] =task1_older["Age"]+ 1


task1_older.to_csv("employees.csv", index = False)

# Task 2 
import json
task2_employees = pd.read_csv("employees.csv")

additional_employees = {
    "Name": ["Eve", "Frank"],
    "Age": [28, 40],
    "City": ["Miami", "Seattle"],
    "Salary": [60000, 95000]}

with open("./additional_employees.json", "w") as file:
    json.dump(additional_employees, file, indent=4)
json_employees= pd.read_json("additional_employees.json")

more_employees = pd.concat([task2_employees , json_employees ], ignore_index= True)


# Task 3 
first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape
print(more_employees.info())

# Task 4
dirty_data = pd.read_csv("./dirty_data.csv")
clean_data = dirty_data.copy()


clean_data = clean_data.drop_duplicates()

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors = "coerce")

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"],  errors = "coerce")


clean_data = clean_data.fillna({"Salary": clean_data["Salary"].median(),"Age": clean_data["Age"].mean()})


clean_data["Hire Date"]= pd.to_datetime(clean_data["Hire Date"], format='mixed')


clean_data["Department"]= clean_data["Department"].str.upper().str.strip()
clean_data["Name"]= clean_data["Name"].str.upper().str.strip()
print(clean_data)