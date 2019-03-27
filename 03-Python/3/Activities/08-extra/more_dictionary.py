
from collections import defaultdict
from collections import Counter

#with a normal dictionary, here's how to count words
words = "hey there hello there whats up wait hello bye hello bye okay okay".split()
d = {}
for w in words:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
print("-"*80)
print("with a normal dictionary")
print(d)
print("-"*80)
# defaultdict lets us initialize the value to any type we choose; in this case, an integer
words = "hey there hello there whats up wait hello bye hello bye okay okay".split()
dd = defaultdict(int)
for w in words:
     dd[w]+=1
print("defaultdict initializes values as integers")
print(dd)
print("-"*80)

#Counter takes a list and counts all the items for us
words = "hey there hello there whats up wait hello bye hello bye okay okay".split()
print("Counter is a dictionary where values are counts of the key value")
c = Counter(words)
print(c)
print("-"*80)