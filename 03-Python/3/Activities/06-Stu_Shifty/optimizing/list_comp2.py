from string import ascii_lowercase
orig_word = input("Enter a shift word: ").lower()
shift_number = int(input("Enter a shift number: "))
shift_number = shift_number % 26

#wrap around back to z for numbers beyond z
#This handles all 3 cases:
# When the shift goes below 'a', 
# when the shift goes above 'z',
word_wrap = [ 
                chr(ord(ascii_lowercase[-1])
                    - ord(ascii_lowercase[0])
                    + ord(c) + shift_number
                    + 1 
                )
                if ord(c) + shift_number < ord(ascii_lowercase[0])
                else 
                    chr(ord(ascii_lowercase[0])
                        + shift_number 
                        - (ord(ascii_lowercase[-1]) - ord(c)) - 1
                       )
                if ord(c) + shift_number > ord(ascii_lowercase[-1])
                else
                chr(ord(c) + shift_number) 
                for c in orig_word
            ]
print("Your ciphered word is {}".format("".join(word_wrap)))