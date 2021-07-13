#cypher
import string
import sys
from typing import final
import numpy as np

#Reset all variables
double = 2
keyCol = "132"
keyRow = "35142"
mes = "Attack at dawn"

#makes invalid all messages longer then the row-column area
if len(mes) > len(keyCol)*len(keyRow):
    print("Invalid Input")
    sys.exit()

#Encrypting a Transposition Cipher
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
    mesList.extend (" " * blankSpace)


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
    

encrypt_Trans (mes, keyCol, keyRow)
