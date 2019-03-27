import string

#list of letters in the list
alphavetical_list =['a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n,','o','p','q','r','s','t','u','v','w','x','y','z']

emptylist=[]

word = input("word to be ciphered")

shiftNumber =int(input("Shift Number?"))

for i in range(0,len(alphavetical_list)-shiftNumber):

    emptylist.append(alphavetical_list[i+shiftNumber])
print(alphavetical_list)




                         