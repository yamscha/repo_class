
# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
csvpath = os.path.join('Resources', 'accounting.csv')


# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        print(row)

