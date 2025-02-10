# Python file detection

import os       # os module = provides a way fpr python programs to operate with Operating Systems

file_path = "FileHandling/test.txt"     # relative file path; absolute file path would be C:\Users\awill\OneDrive\Documents\Python Practice\FileHandling\test.txt; \t = tab, so use double slashes or forward slash instead 

if os.path.exists(file_path):                   # use if statement, access os module, access path, use built-in method 'exists' and pass in file path as the arg; returns a boolean 
    print(f"The location '{file_path}' exists.")

    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):              # is dir is a method to check if something is a directory
        print("That is a directory.")
else:
    print("That location does not exist.")