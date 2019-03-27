import os
csvpath = os.path.join('Resources', 'accounting.csv')


 # Method 1: Plain Reading of CSVs
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))