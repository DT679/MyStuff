##user input
key = "thequickbrownfoxjumpsoverthelazydog"
Message = raw_input('please enter your message no spaces :):')
MessageLength = len(Message)
if len(Message)<= len(key):
    print "length of message can work but would be better if =35, let's go with the length you entered: ", MessageLength
else:
    print "please start over and enter only 35 characters. Goodbye"



MNumbers = []

for letter in Message:

  number = ord(letter) - 96

  MNumbers.append(number)


#print "here are the message numbers as a tuple", tuple(MNumbers)


##truncate key


truncated_key = key[0:MessageLength]


#print "this is the pad we will use", (truncated_key)



KNumbers = []

for letter in truncated_key:

  number = ord(letter) - 96

  KNumbers.append(number)


#print "here is truncated key as a tuple", tuple(KNumbers)


## add the string of tuples together

CipherTuple = [x + y for x, y in zip(MNumbers, KNumbers)]


#print "here is cipher tuple", (CipherTuple)

    


CipherList = list (CipherTuple)
#print "here is CipherList;", (CipherList)
new_list = []
for number in (CipherList):
    while number > 26:
        number -= 26
    new_list.append(number)
    #print new_list





character_list = [chr(number + 96) for number in (new_list)]
#print "here is character list", (character_list)

print("Encrypted message:")
print("".join(character_list))












