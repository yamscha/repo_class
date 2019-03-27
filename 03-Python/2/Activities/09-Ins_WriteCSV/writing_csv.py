import os
import csv

output_path = os.path.join('output','test.csv')

item_list = [[1, 2, 3, 4] ,
             ["Michael", "Dwight", "Meredith", "Kelly"],
             ["Boss", "Sales", "Sales", "HR"]]
# Zip all three lists together into tuples
#roster = zip(indexes, employees, department)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
# Write the first row (column headers)
    #for employee in employees:
    csvwriter.writerows(item_list)

