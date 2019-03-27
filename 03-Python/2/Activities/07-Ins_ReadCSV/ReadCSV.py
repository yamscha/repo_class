
# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
csvpath = os.path.join('Resources', 'accounting.csv')

# Method 2: Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:
#what is that newline='' argument doing?  Let's ask the internet!
#https://docs.python.org/3/library/functions.html#open

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        print(row)
    print(type(row))
