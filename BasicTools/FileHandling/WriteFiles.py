
# txt files

txt_data = "This is some text."

file_path = "output.txt"         

with open(file_path, "w") as file:              # with = a statement used to wrap a block of code to execute
    file.write(txt_data)                            
    print(f"txt file '{file_path}' was created.")  
                                                    
                                            

try:
    with open(file_path, "x") as file:          # creates a new file if one does not already exist
        file.write(txt_data)
        print(f"txt file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.") 

try:
    with open(file_path, "a") as file:
        file.write("\n" + txt_data)             # appending new text data
        print(f"txt file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.") 


#list:
employees = ["employee1", "employee2", "employee3"]

try:
    with open(file_path, "x") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created.")
except FileExistsError:
    print("That file already exists.") 

# json files

import json

#dictionary:
student = {
    "name": "Glorbnt",
    "age": 12,
    "gpa": 2.8
}

file_path2 = "output2.json"

try:
    with open(file_path2, "x") as file2:
        json.dump(student, file2, indent=4)    
        print(f"json file '{file_path2}' was created.")
except FileExistsError:
    print("That file already exists.") 


# csv files

import csv

# 2D data structure:

workers = [["Name", "Age", "Salary"],
           ["Name1", 22, 24],
           ["Name2", 26, 25],
           ["Name3", 33, 22]
]

file_path3 = "output3.csv"
try:
    with open(file_path3, "w", newline="") as file3:       
        writer = csv.writer(file3)
        print(f"csv file '{file_path3}' was created.")
        for row in workers:
            writer.writerow(row)               
except FileExistsError:
    print("That file already exists.") 

