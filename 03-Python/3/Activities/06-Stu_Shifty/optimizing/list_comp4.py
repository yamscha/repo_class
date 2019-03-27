from string import ascii_lowercase
orig_word = input("Enter a shift word: ").lower()
shift_number = int(input("Enter a shift number: ")) % 26
#remember that 27 % 26 is 1
#in Python, -27 % 26 is +25
print("your cipher is {}".format(
            "".join(
                    [
                        ascii_lowercase[ord(c) + shift_number - ord(ascii_lowercase[0])] 
                        if 
                            ord(c) + shift_number - ord(ascii_lowercase[0]) < len(ascii_lowercase)
                        else 
                            ascii_lowercase[ord(c) 
                            - ord(ascii_lowercase[0]) 
                            + shift_number 
                            - len(ascii_lowercase)]
                        for c in orig_word
                    ]
                   )))
