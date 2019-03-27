# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

print("Think of these as the columns of data")
print(indexes)
print(employees)
print(department)

# Zip all three lists together into tuples
roster = zip(indexes, employees, department)

print("Think of zip as creating the rows of data")
# Print the contents of each row
for employee in roster:
    print(employee)

print(type(employee))