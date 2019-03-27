
# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer
age = int(input("How old are you? "))

# Collects the user's input for the prompt "Is this statement true?" and converts it to a boolean
# any non-empty string is converted to True;
# only an empty string (no input) is False
trueOrFalse = bool(input("Is this statement true? (any non-empty string evaluates to True; empty string evaluates to False:"))

# Creates three print statements that to respond with the output
print("My name is " + str(name))
print("I am " + str(age) + " years old.")
print("The statement was " + str(trueOrFalse))

