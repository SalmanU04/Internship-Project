#Coder/Decoder
import sys
import string
from typing import no_type_check
import time

"""
Set all variable equal to NOT
Ask for Whether they will code or decode (Encrypt or Decrypt)
Ask for message
alphabet set to all letter (upper and lower)
Brute Force and Key will be determined later
"""

message = input("What is your message: ")
decodeOrCode = int(input("Do you want to code (0) or decode (1)?"))
decode = 0
code = 0
key = 0
bruteForce = 0
newMessage = []
oldMessage = []
alphabet = string.ascii_letters + "0123456789.,!?"

#----------------------------------------------------------------------------------------------------------
#define Encryption and Decryption Variables
def encrypt(alphabet, shiftKey, message, newMessage):
    newMessage = []
    shift = {}
    #Alphabet will be shifted by the user's key (if they have one)
    for x in range(len(alphabet)):
        shift[alphabet[x]] = alphabet[(x+shiftKey)%len(alphabet)]
    for char in message:
        if char in alphabet:
            change = shift[char]
            newMessage.append(change)
        else: 
            change = char 
            newMessage.append(change)
    newMessage = "".join(newMessage)
    print (newMessage)

def decrypt(alphabet, shiftKey, message, oldMessage):
    oldMessage = []
    shift = {}
    for x in range(len(alphabet)):
        shift[alphabet[x]] = alphabet[(x-shiftKey)%len(alphabet)]
    for char in message:
        if char in alphabet:
            change = shift[char]
            oldMessage.append(change)
        else: 
            change = char 
            oldMessage.append(change)
    oldMessage = "".join(oldMessage)
    if bruteForce == 1: 
        print (str(shiftKey) + ": " + oldMessage)
    else: 
        print (oldMessage)

#----------------------------------------------------------------------------------------------------------

if decodeOrCode == 0:
    code = 1
elif decodeOrCode == 1:
    decode = 1
else: 
    print ("Invalid Input")
    sys.exit()


ask_key = str(input("Do you have a key? (Y/N) "))

if ask_key == "Y":
    key = 1
elif ask_key == "N":
    key = 0    
else:
    print ("Invalid Input")
    sys.exit

if key == 1 and decode == 1:
    shiftKey = int(input ("What is your key-shift? "))
    decrypt (alphabet, shiftKey, message, oldMessage)
elif key == 0 and decode == 1:
    bruteForce = 1
elif key == 1 and code == 1:
    shiftKey = int(input ("What is your key-shift? "))
    encrypt (alphabet, shiftKey, message, oldMessage)
elif key == 0 and code == 1:
    print ("Invalid Input")
    sys.exit

#----------------------------------------------------------------------------------------------------------
#Brute Force attack

if bruteForce == 1:
    x = 1
    print ("We will have to do a Brute Force attack")
    time.sleep(3)
    while x != 27:
        decrypt (alphabet, x, message, oldMessage)
        x += 1
    else:
        sys.exit

"""
Now time for keys not in
"""
        