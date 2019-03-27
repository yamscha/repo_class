#A way to shift letters: e.g. a + 2 -> c

import string
orig_word = input("Enter a shift word: ").lower()
shift_number = int(input("Enter a shift number: "))
#to avoid index out of bounds, keep shift from exceeding 27
shift_number = shift_number % 26

print(string.ascii_lowercase)
ascii_a = ord(string.ascii_lowercase[0]) #97
ascii_z = ord(string.ascii_lowercase[-1]) #122

#convert characters to their ascii integers
word_ascii = [ord(c) for c in orig_word]
print(word_ascii)

#shift integers
word_ascii_shifted = [i+shift_number for i in word_ascii]
print(word_ascii_shifted)

#wrap around back to z for numbers beyond z
#This handles all 3 cases:
# When the shift goes below 'a', 
# when the shift goes above 'z',
# when the shift stays within a and z
word_ascii_wrap = [ ascii_z - (i - ascii_a) 
                    if i < ascii_a 
                    else ascii_a + (i - ascii_z) - 1 
                    if i > ascii_z
                    else i
                    for i in word_ascii_shifted]
print(word_ascii_wrap)

#turn it back to letters
word_wrap = [chr(i) for i in word_ascii_wrap]
print(word_wrap)

#convert list of characters back to a string
print("your ciphered word is {}".format("".join(word_wrap)))
