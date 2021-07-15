<<<<<<< HEAD
#Coder/Decoder
import sys
import string
from typing import no_type_check
import time
from typing import final
import numpy as np

"""
Set all variable equal to NOT
Ask for Whether they will code or decode (Encrypt or Decrypt)
Ask for message
alphabet set to all letter (upper and lower)
Brute Force and Key will be determined later
"""
typeOfCipher = int(input("Will you do a Transposition Cipher (0) or a Shift Cipher (1)? "))
message = input("What is your message: ")
decodeOrCode = int(input("Do you want to code (0) or decode (1)?"))
decode = 0
code = 0
key = 0
bruteForce = 0
newMessage = []
oldMessage = []
double = 2
keyCol = ""
keyRow = ""
alphabet = string.ascii_letters + "0123456789.,!?"

##############################################################################################################
#define Encryption and Decryption Variables for shift
def encrypt_shift(alphabet, shiftKey, message, newMessage):
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

def decrypt_shift(alphabet, shiftKey, message, oldMessage):
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

##############################################################################################################
#Encrypt for a transposition cipher

def encrypt_Trans (mes, keyCol, keyRow):

    #Length of message, column and row is found. 
    mesLen = len(mes)
    col = len(keyCol)
    row = len(keyRow)
    
    #sets the row and column both to integers, then uses them to create the sorted order
    rowOrder = [int(x) for x in str(keyRow)]
    ogRowOrder = sorted(list(rowOrder))
    
    
    colOrder = [int(x) for x in str(keyCol)]
    ogColOrder = sorted(list(colOrder))

    #checks for double to determine row length...
    if double == 2:
        row = len(keyRow)
    elif double == 1:
        row = int((mesLen/col)+(1-((mesLen%col)/col)))
        print (row)


    #message is converted to a list, and blank spaces are added to the ends of the list to fill
    mesList = list(mes)
    blankSpace = ((row * col) - mesLen)
    mesList.extend ("_" * blankSpace)
    for x, y in enumerate(mesList):
        if y == " ":
            mesList[x] = "_"


    #sets list to a matrix
    mesMat = [mesList[x: x+col] for x in range(0, len(mesList), col)]

    #creates 3 variables (mesMat is the original, newArray is for the col, and final array is for the row.
    #Final array is also output). All variables are converted to numpy arrays
    newArray = np.array(mesMat).reshape (row, col)    
    finalArray = np.array(mesMat).reshape (row, col)
    mesMat = np.array(mesMat)
    
    #Swaps Column
    def swap_col (array, newArray, start, last):
        newArray[:, [start]] = array [:,[last]]
    
    #Swaps Row
    def swap_row (array, newArray, start, last):
        newArray[[start],:] = array[[last],:]
    #newArray takes from the original array in both. 
    
    # 
    for x in range(len(keyCol)):   
        swap_col (mesMat, newArray, ogColOrder[x]-1, colOrder[x]-1)
    for x in range (len(keyRow)):
        swap_row (newArray, finalArray, ogRowOrder[x]-1, rowOrder[x]-1)

    #This will convert the array into a readable string
    cipher = finalArray.astype('|S1').tobytes().decode('utf-8')
    print (cipher)

def decrypt_Trans (mes, keyCol, keyRow):
    #Length of message, column and row is found. 
    mesLen = len(mes)
    col = len(keyCol)
    row = len(keyRow)
    
    #sets the row and column both to integers, then uses them to create the sorted order
    rowOrder = [int(x) for x in str(keyRow)]
    ogRowOrder = sorted(list(rowOrder))
    
    
    colOrder = [int(x) for x in str(keyCol)]
    ogColOrder = sorted(list(colOrder))

    #checks for double to determine row length...
    if double == 2:
        row = len(keyRow)
    elif double == 1:
        row = int((mesLen/col)+(1-((mesLen%col)/col)))
        print (row)


    #message is converted to a list, and blank spaces are added to the ends of the list to fill
    mesList = list(mes)
    blankSpace = ((row * col) - mesLen)
    mesList.extend ("_" * blankSpace)
    for x, y in enumerate(mesList):
        if y == " ":
            mesList[x] = "_"


    #sets list to a matrix
    mesMat = [mesList[x: x+col] for x in range(0, len(mesList), col)]

    #creates 3 variables (mesMat is the original, newArray is for the col, and final array is for the row.
    #Final array is also output). All variables are converted to numpy arrays
    newArray = np.array(mesMat).reshape (row, col)    
    finalArray = np.array(mesMat).reshape (row, col)
    mesMat = np.array(mesMat)
    
    #Swaps Column
    def swap_col (array, newArray, start, last):
        newArray[:, [last]] = array [:,[start]]
    
    #Swaps Row
    def swap_row (array, newArray, start, last):
        newArray[[last],:] = array[[start],:]
    #newArray takes from the original array in both. 
    
    # 
    for x in range(len(keyCol)):   
        swap_col (mesMat, newArray, ogColOrder[x]-1, colOrder[x]-1)
    for x in range (len(keyRow)):
        swap_row (newArray, finalArray, ogRowOrder[x]-1, rowOrder[x]-1)

    #This will convert the array into a readable string
    cipher = finalArray.astype('|S1').tobytes().decode('utf-8')
    print (cipher)
##############################################################################################################

#Determines wheteher to code or decode
if decodeOrCode == 0:
        code = 1
elif decodeOrCode == 1:
    decode = 1
else: 
    print ("Invalid Input (Please type either '0' or '1')")
    sys.exit()

#If the user asks for a Shift Cipher then...
if typeOfCipher == 1:

    ask_key = str(input("Do you have a key? (Y/N) "))

    if ask_key == "Y":
        key = 1
    elif ask_key == "N":
        key = 0    
    else:
        print ("Invalid Input (Type either 'Y' or 'N')")
        sys.exit()

    if key == 1 and decode == 1:
        shiftKey = int(input ("What is your key-shift? "))
        decrypt_shift (alphabet, shiftKey, message, oldMessage)
    elif key == 0 and decode == 1:
        bruteForce = 1
    elif key == 1 and code == 1:
        shiftKey = int(input ("What is your key-shift? "))
        encrypt_shift (alphabet, shiftKey, message, oldMessage)
    elif key == 0 and code == 1:
        print ("Invalid Input (Not possible to encrypt without a key)")
        sys.exit()

#If the user asks for a Transposition Cipher then...
elif typeOfCipher == 0:
    doubleAsk = str(input ("Will you use a double cipher? (Y/N) "))
    if doubleAsk == "Y":
        double = 2
    elif doubleAsk == "N":
        double = 1
    else:
        print ("Invalid Input (Type either 'Y' or 'N')")
        sys.exit()

    if double == 1:
        keyCol = int(input("What is your column key? "))
    elif double == 2:
        keyRow = int(input ("What is your row key? "))
        keyCol = int(input("What is your column key? "))

    keyRow = str(keyRow)
    keyCol = str(keyCol)

    #makes invalid all messages longer then the row-column area
    if double == 2:
        if len(message) > len(keyCol)*len(keyRow):
            print("Invalid Input (Message too long)")
            sys.exit()
    
    
    if decode == 1:
        decrypt_Trans (message, keyCol, keyRow)
    elif code == 1:
        encrypt_Trans (message, keyCol, keyRow)
##############################################################################################################
#Brute Force attack

if bruteForce == 1:
    x = 1
    print ("We will have to do a Brute Force attack")
    time.sleep(3)
    while x != 27:
        decrypt_shift (alphabet, x, message, oldMessage)
        x += 1
    else:
        sys.exit()
=======
#Coder/Decoder
import sys
import string
from typing import no_type_check
import time
from typing import final
import numpy as np

"""
Set all variable equal to NOT
Ask for Whether they will code or decode (Encrypt or Decrypt)
Ask for message
alphabet set to all letter (upper and lower)
Brute Force and Key will be determined later
"""
typeOfCipher = int(input("Will you do a Transposition Cipher (0) or a Shift Cipher (1)? "))
message = input("What is your message: ")
decodeOrCode = int(input("Do you want to code (0) or decode (1)?"))
decode = 0
code = 0
key = 0
bruteForce = 0
newMessage = []
oldMessage = []
double = 2
keyCol = ""
keyRow = ""
alphabet = string.ascii_letters + "0123456789.,!?"

##############################################################################################################
#define Encryption and Decryption Variables for shift
def encrypt_shift(alphabet, shiftKey, message, newMessage):
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

def decrypt_shift(alphabet, shiftKey, message, oldMessage):
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

##############################################################################################################
#Encrypt for a transposition cipher

def encrypt_Trans (mes, keyCol, keyRow):

    #Length of message, column and row is found. 
    mesLen = len(mes)
    col = len(keyCol)
    row = len(keyRow)
    
    #sets the row and column both to integers, then uses them to create the sorted order
    rowOrder = [int(x) for x in str(keyRow)]
    ogRowOrder = sorted(list(rowOrder))
    
    
    colOrder = [int(x) for x in str(keyCol)]
    ogColOrder = sorted(list(colOrder))

    #checks for double to determine row length...
    if double == 2:
        row = len(keyRow)
    elif double == 1:
        row = int((mesLen/col)+(1-((mesLen%col)/col)))
        print (row)


    #message is converted to a list, and blank spaces are added to the ends of the list to fill
    mesList = list(mes)
    blankSpace = ((row * col) - mesLen)
    mesList.extend ("_" * blankSpace)
    for x, y in enumerate(mesList):
        if y == " ":
            mesList[x] = "_"


    #sets list to a matrix
    mesMat = [mesList[x: x+col] for x in range(0, len(mesList), col)]

    #creates 3 variables (mesMat is the original, newArray is for the col, and final array is for the row.
    #Final array is also output). All variables are converted to numpy arrays
    newArray = np.array(mesMat).reshape (row, col)    
    finalArray = np.array(mesMat).reshape (row, col)
    mesMat = np.array(mesMat)
    
    #Swaps Column
    def swap_col (array, newArray, start, last):
        newArray[:, [start]] = array [:,[last]]
    
    #Swaps Row
    def swap_row (array, newArray, start, last):
        newArray[[start],:] = array[[last],:]
    #newArray takes from the original array in both. 
    
    # 
    for x in range(len(keyCol)):   
        swap_col (mesMat, newArray, ogColOrder[x]-1, colOrder[x]-1)
    for x in range (len(keyRow)):
        swap_row (newArray, finalArray, ogRowOrder[x]-1, rowOrder[x]-1)

    #This will convert the array into a readable string
    cipher = finalArray.astype('|S1').tobytes().decode('utf-8')
    print (cipher)

def decrypt_Trans (mes, keyCol, keyRow):
    #Length of message, column and row is found. 
    mesLen = len(mes)
    col = len(keyCol)
    row = len(keyRow)
    
    #sets the row and column both to integers, then uses them to create the sorted order
    rowOrder = [int(x) for x in str(keyRow)]
    ogRowOrder = sorted(list(rowOrder))
    
    
    colOrder = [int(x) for x in str(keyCol)]
    ogColOrder = sorted(list(colOrder))

    #checks for double to determine row length...
    if double == 2:
        row = len(keyRow)
    elif double == 1:
        row = int((mesLen/col)+(1-((mesLen%col)/col)))
        print (row)


    #message is converted to a list, and blank spaces are added to the ends of the list to fill
    mesList = list(mes)
    blankSpace = ((row * col) - mesLen)
    mesList.extend ("_" * blankSpace)
    for x, y in enumerate(mesList):
        if y == " ":
            mesList[x] = "_"


    #sets list to a matrix
    mesMat = [mesList[x: x+col] for x in range(0, len(mesList), col)]

    #creates 3 variables (mesMat is the original, newArray is for the col, and final array is for the row.
    #Final array is also output). All variables are converted to numpy arrays
    newArray = np.array(mesMat).reshape (row, col)    
    finalArray = np.array(mesMat).reshape (row, col)
    mesMat = np.array(mesMat)
    
    #Swaps Column
    def swap_col (array, newArray, start, last):
        newArray[:, [last]] = array [:,[start]]
    
    #Swaps Row
    def swap_row (array, newArray, start, last):
        newArray[[last],:] = array[[start],:]
    #newArray takes from the original array in both. 
    
    # 
    for x in range(len(keyCol)):   
        swap_col (mesMat, newArray, ogColOrder[x]-1, colOrder[x]-1)
    for x in range (len(keyRow)):
        swap_row (newArray, finalArray, ogRowOrder[x]-1, rowOrder[x]-1)

    #This will convert the array into a readable string
    cipher = finalArray.astype('|S1').tobytes().decode('utf-8')
    print (cipher)
##############################################################################################################

#Determines wheteher to code or decode
if decodeOrCode == 0:
        code = 1
elif decodeOrCode == 1:
    decode = 1
else: 
    print ("Invalid Input (Please type either '0' or '1')")
    sys.exit()

#If the user asks for a Shift Cipher then...
if typeOfCipher == 1:

    ask_key = str(input("Do you have a key? (Y/N) "))

    if ask_key == "Y":
        key = 1
    elif ask_key == "N":
        key = 0    
    else:
        print ("Invalid Input (Type either 'Y' or 'N')")
        sys.exit()

    if key == 1 and decode == 1:
        shiftKey = int(input ("What is your key-shift? "))
        decrypt_shift (alphabet, shiftKey, message, oldMessage)
    elif key == 0 and decode == 1:
        bruteForce = 1
    elif key == 1 and code == 1:
        shiftKey = int(input ("What is your key-shift? "))
        encrypt_shift (alphabet, shiftKey, message, oldMessage)
    elif key == 0 and code == 1:
        print ("Invalid Input (Not possible to encrypt without a key)")
        sys.exit()

#If the user asks for a Transposition Cipher then...
elif typeOfCipher == 0:
    doubleAsk = str(input ("Will you use a double cipher? (Y/N) "))
    if doubleAsk == "Y":
        double = 2
    elif doubleAsk == "N":
        double = 1
    else:
        print ("Invalid Input (Type either 'Y' or 'N')")
        sys.exit()

    if double == 1:
        keyCol = int(input("What is your column key? "))
    elif double == 2:
        keyRow = int(input ("What is your row key? "))
        keyCol = int(input("What is your column key? "))

    keyRow = str(keyRow)
    keyCol = str(keyCol)

    #makes invalid all messages longer then the row-column area
    if double == 2:
        if len(message) > len(keyCol)*len(keyRow):
            print("Invalid Input (Message too long)")
            sys.exit()
    
    
    if decode == 1:
        decrypt_Trans (message, keyCol, keyRow)
    elif code == 1:
        encrypt_Trans (message, keyCol, keyRow)
##############################################################################################################
#Brute Force attack

if bruteForce == 1:
    x = 1
    print ("We will have to do a Brute Force attack")
    time.sleep(3)
    while x != 27:
        decrypt_shift (alphabet, x, message, oldMessage)
        x += 1
    else:
        sys.exit()
>>>>>>> 20d2c2348bcb59a1eeb39a442e7e65627f701cb4
        