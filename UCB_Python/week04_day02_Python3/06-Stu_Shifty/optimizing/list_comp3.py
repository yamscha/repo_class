from string import ascii_lowercase
orig_word = input("Enter a shift word: ").lower()
shift_number = int(input("Enter a shift number: "))
#remember that 27 % 26 is 1
#in Python, -27 % 26 is +25
shift_number = shift_number % 26
alphabet_indices = [ord(c) - ord(ascii_lowercase[0]) for c in orig_word]
print(alphabet_indices)

alphabet_indices_shifted = [i+shift_number for i in alphabet_indices ]
print(alphabet_indices_shifted)

alphabet_indices_wrap = [i if i < len(ascii_lowercase) 
                        else i - len(ascii_lowercase)
                        for i in alphabet_indices_shifted]
print(alphabet_indices_wrap)

letters_wrap = [ascii_lowercase[i] for i in alphabet_indices_wrap]
print(letters_wrap)

print("Your ciphered word is {}".format("".join(letters_wrap)))