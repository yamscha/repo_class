#sets contain unique values
#think of them like dictionaries where the key is also the value

l = "stop repeating yourself stop repeating yourself stop repeating yourself".split()
s = set(l)
print("-"*80)
print("original list")
print(l)
print("-"*80)
print("the set")
print(s)
print("-"*80)
#when adding to a set, use .add (.append is for lists)
s2 = set()
for w in l:
    s2.add(w)
print("set 2")
print(s2)
print("-"*80)

#you can fill a list with a set
l2 = list(s2)
print("this is a list made from a set")
print(l2)
print("-"*80)