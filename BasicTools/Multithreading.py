# multithreading = Used to perform multiple tasks concurrently (Good for I/O bound tasks like reading files, fetching data from APIs, etc.)

import threading
import time


def function1():
    time.sleep(3)     
    print("This task is complete")

def function2():
    time.sleep(2)
    print("This task is complete")

def function3():
    time.sleep(1)
    print("This task is complete")


# chore that takes the least amount of time will finish first:

task1 = threading.Thread(target=function1)
task1.start()

task2 = threading.Thread(target=function2)
task2.start()

task3 = threading.Thread(target=function3)
task3.start()

# print a confirmation message when all chores are complete (use join method to ensure it prints after the chores)

task1.join()
task2.join()
task3.join()

print("All tasks are complete")

# include args as a tuple for functions with multiple arguments:

def function4(arg1):
    print(f"{arg1} is complete")

def function5(arg2, arg3):
    print(f"{arg2} and {arg3} are complete")


task4 = threading.Thread(target=function4, args=("arg1",))   # **remember to include comma to distinguish it as a tuple
task5 = threading.Thread(target=function5, args=("arg2", "arg3"))
