#cypher
import string

import numpy as np
"""
ask_Key = input ("What is your key:")
message = input ("What is your message")

letters = string.ascii_lowercase 

letters = list(letters)

if '1' and '2' and '3' and '4' in ask_Key:
    print("Good")
elif len(ask_Key) == 4:
    print ("Even better")

"""
#Reset all variables
double = 1
keyCol = "132"
keyRow = "35142"
mes = "Attack at dawn"

#Encrypting a Transposition Cipher
def encrypt_Trans (mes, keyCol, keyRow):
    cipher = ""


    mesLen = len(mes)
    col = len(keyCol)
    row = len(keyRow)
    #rowInt = int(keyRow)
    rowOrder = [int(x) for x in str(keyRow)]
    print (rowOrder)
    #colInt = int(keyCol)
    colOrder = [int(x) for x in str(keyCol)]
    print (colOrder)
    ogColOrder = []

    for i in range (col):
        ogColOrder.append(i+1)

    print (ogColOrder)


    if double == 2:
        row = len(keyRow)
    elif double == 1:
        row = int((mesLen/col)+(1-((mesLen%col)/col)))
    
    print (row)


    mesList = list(mes)
    blankSpace = ((row * col) - mesLen)
    mesList.extend (" " * blankSpace)

    print (mesList)

    mesMat = [mesList[x: x+col] for x in range(0, len(mesList), col)]
    print (mesMat)
    mesMat = np.array(mesMat).reshape (row, col)
    def swap_col (array, start, last):
        array [:, [start]] = array [:,[last]]
    
    for x in range(len(keyCol)):
        swap_col (mesMat, ogColOrder[x]-1, colOrder[x]-1)

    print (mesMat)

encrypt_Trans (mes, keyCol, keyRow)
