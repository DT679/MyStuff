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



#characters = [unichr(n + 96) for n in (CipherList)]
#print "herearechar;", (characters)



#CipherList = []
#for item in (CipherTuple):
#   TupleToList = item
#   CipherList.append(TupleToList)
#print (CipherList)

## turn list to int
#CipherInt = [ord(i) for i in (CipherTuple)]
#print "Int List is:", (CipherInt)


#print [ord(char) - 96 for char in (CipherInt)]

#CipherStr = str(CipherList)
#print "hereiscipherstr", (CipherStr)
## turn cipher string into letters
#EncrypNum[]
#for item in (CipherStr)
    

## turn list to int
#CipherInt = [int(i) for i in (CipherList)]
#print "Int List is:", (CipherInt)




#IntList = int(',' .join(map(str, list(CipherTuple))))

#print "here is IntList", IntList

## encrypt
#EncMess = chr(CipherStr)
#print "here is the encrypted message", (EncMess)


### - i need to get the tuple in a list. convert the list to letters then combine the letters for the encryption.







    

#Convert tuple to list
#CipherList = [int(i) for i in (CipherTuple)]
#print "here is cipherlist", int(CipherList)
#print "here is encryption", chr(CipherList)


 

#attempt to encrypt

#Encrypt = []

#for number in CipherList:

#  letter = chr(number) - 96

#  Encrypt.append(letter)

#print "here is encryption", Encrypt


## encrypt
#EncMess = chr(SCipherList)
#print "here is the encrypted message", (EncMess)







