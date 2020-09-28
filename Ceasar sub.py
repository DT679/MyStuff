

print "Welcome to Donna Pinion's Ceasar Cipher for CS 636"

message = raw_input('Please enter your message:')

ikey = 3


def encrypt(message,ikey): 
    output = "" 
  
    for i in range(len(message)): 
        char = message[i]

        if (char.isupper()): 
            output += chr((ord(char) + ikey -65) % 26 + 65) 
    
        else: 
            output += chr((ord(char) + ikey - 97) % 26 + 97) 
  
    return output 
print "Cipher output: " + encrypt (message,ikey)



