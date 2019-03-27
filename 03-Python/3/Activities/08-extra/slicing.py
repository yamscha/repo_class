
#slice lists:

l = [i for i in range(10)]
print(l)
print(l[0:2])
print(l[:2])

#you can index backwards from the end of a list
print(l[-2:])

#slice in steps
print(l[0:8:2])

#here's how to reverse a list!
print(l[::-1])