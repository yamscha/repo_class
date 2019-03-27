#A way to shift letters: e.g. a + 2 -> c

import string
orig_word = input("Enter a shift word: ").lower()
shift_number = int(input("Enter a shift number: "))
#to avoid index out of bounds, keep shift from exceeding 27
#also 27 % 26 -> +1
#notice that -1 % 26 -> +25 ; this is specific to Python and not all languages
#http://yourdailygeekery.com/2011/06/28/modulo-of-negative-numbers.html
shift_number = shift_number % 26
print(shift_number)
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
word_ascii_wrap = [i if i<=ascii_z else ascii_a + (i - ascii_z) - 1 
                    for i in word_ascii_shifted]
print(word_ascii_wrap)

#turn it back to letters
word_wrap = [chr(i) for i in word_ascii_wrap]
print(word_wrap)

#convert list of characters back to a string
print("your ciphered word is {}".format("".join(word_wrap)))
