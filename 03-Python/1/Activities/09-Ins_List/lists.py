# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
myotherlist = list()
myotherlist2 = []
print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

# Changes a specified element within an List at the given index
myList[3] = 85
print(myList)

# Returns the index of the first object with a matching value
print(myList.index("Matt"))

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Matt")
print(myList)

# Removes the object at the index specified
myList.pop(0)
myList.pop(0)
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)



#list of lists

my_lol = []
l1 = [1,2,3]
l2 = [4,5,6]
my_lol.append(l1)
my_lol.append(l2)
print(my_lol)
print(my_lol[0][1])