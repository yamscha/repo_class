# Store the file path associated with the file (note the backslash may be OS specific) 
file_name = 'Resources/input.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file_name, 'r') as file_object:

    print("what is file_object var?")
    print(file_object)

    print("read all lines")
    # Store all of the text inside a variable called "lines"
    lines = file_object.read()

    # Print the contents of the text file
    print(lines)

print("\nread one line at a time\n")
with open("Resources/accounting.csv", 'r') as f:
    for line in f.readlines():
        print(line,end='')

