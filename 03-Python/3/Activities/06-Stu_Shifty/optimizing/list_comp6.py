from string import ascii_lowercase
orig_word = input("Enter a shift word: ").lower()
shift_number = int(input("Enter a shift number: ")) % 26
#this is one statement; it can be put on one line
print("your cipher is {}".format("".join( [ ascii_lowercase[(ord(c) + shift_number - ord(ascii_lowercase[0]))%26] for c in orig_word ])))