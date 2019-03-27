from string import ascii_lowercase

print(ascii_lowercase)
for i, l in enumerate(ascii_lowercase):
    print("{}:{}".format(i,l))

for i in range(len(ascii_lowercase)):
    val = ascii_lowercase[i]
    print("{}:{}".format(i,val))

words = "the quick brown fox jumps over the lazy dog".split()
print(words)

#you'll see these dictionaries a lot in natural language processing
#this is also using dictionary comprehension
idx_to_words = {i:w for i,w in enumerate(words)}
print("idx_to_words")
print(idx_to_words)

words_to_idx = {w:i for i,w in enumerate(words)}
print("words_to_idx")
print(words_to_idx)