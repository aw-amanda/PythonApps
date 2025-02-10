# Python reading files (.txt, .json, .csv)

file_path = "output.txt"

# Read a txt file:

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError: 
    print("File not found.")
except PermissionError:
    print("You do not have permission to read this file.")

# Read a json file:

import json

file_pathJ = "output.json"

try:
    with open(file_pathJ, "r") as fileJ:
        content = json.load(fileJ)
        print(content["name"])
except FileNotFoundError: 
    print("File not found.")
except PermissionError:
    print("You do not have permission to read this file.")


# Read a csv file:

import csv

file_pathC = "output.csv"

try:
    with open(file_pathC, "r") as fileC:
        content = csv.reader(fileC)
        for line in content:
            print(line[0])
except FileNotFoundError: 
    print("File not found.")
except PermissionError:
    print("You do not have permission to read this file.")