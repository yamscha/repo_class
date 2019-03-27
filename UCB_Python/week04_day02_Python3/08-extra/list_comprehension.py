
#list comprehensions run faster than for loops

l1 = [0 for i in range(5)]
print("l1")
print(l1)
l2 = [i for i in range(5)]
print("l2")
print(l2)
l3 = [c for c in "abc"]
print("l3")
print(l3)

#list comprehensions with conditionals
l4 = ['apples' if i < 2 else 'bananas' for i in range(5)]
print("l4")
print(l4)
l5 = ['apples' if i < 2 else 'bananas' if i < 3 else 'oranges' for i in range(5)]
print("l5")
print(l5)

