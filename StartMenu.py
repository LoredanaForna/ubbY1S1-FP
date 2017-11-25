'''
Created on 30 Oct 2017

@author: Lore
'''
import Features
from ImportantFunctions import addNumber
from ImportantFunctions import remove1
from ImportantFunctions import insertNumber
from ImportantFunctions import sortedValues
from ImportantFunctions import mul
from Features import removeIndex
from Features import  replaceValue
from Features import  printValue
from Features import  sortedAndGreater
from Features import avgNumbers
from Features import  minScore
from Features import multiples
from Features import deleteLower
from Features import deleteValue


def printMenu():
    menuStr="\n Menu: \n"
    menuStr+="\t Press 1 - Add a value in the list \n"
    menuStr+="\t Press 2 - Insert a value on a specific index i \n"
    menuStr+="\t Press 3 - Remove the value from a specific index \n"
    menuStr+="\t Press 4 - Remove the values from index i to index j \n"
    menuStr+="\t Press 5 - Replace the value from index i with another value \n"
    menuStr+="\t Press 6 - Print the indexes with values less than n \n"
    menuStr+="\t Press 7 - Print all indexes sorted by their value(sorted list) \n"
    menuStr+="\t Press 8 - Print the indexes with values higher than n(sorted list) \n"
    menuStr+="\t Press 9 - Print the average of values for indexes i..j \n"
    menuStr+="\t Press 10 - Print the smallest value for indexes i..j \n"
    menuStr+="\t Press 11 - Print the values for indexes i..j which are multiples of n \n"
    menuStr+="\t Press 12 - Delete the values that are not a multiples of n \n"
    menuStr+="\t Press 13 - Delete the values that are less or equal to n \n"
    menuStr+="\t Press 14 - Undo the last operation that modified the list \n"
    menuStr+="\t 0-Exit "
    print(menuStr)

def startProgram():
    my_list=[10,41,80,5,20,14,400,70]
    print("\n My list is: [10,41,80,5,20,14,400,70] \n")
    printMenu()
    global prev_list
    while(True):
        option=int(input("Enter an option:"))
        if option==0:
            break
        elif option==1:
            prev_list=my_list[:]
            addNumber(my_list) 
        elif option==2:
            prev_list=my_list[:]
            insertNumber(my_list)
        elif option==3:
            prev_list=my_list[:]
            remove1(my_list)
        elif option==4:
            prev_list=my_list[:]
            removeIndex(my_list)
        elif option==5:
            prev_list=my_list[:]
            replaceValue(my_list)
        elif option==6:
            prev_list=my_list[:]
            printValue(my_list)
        elif option==7:
            prev_list=my_list[:]
            sortedValues(my_list)
        elif option==8:
            prev_list=my_list[:]
            sortedAndGreater(my_list)
        elif option==9:
            prev_list=my_list[:]
            avgNumbers(my_list)
        elif option==10:
            prev_list=my_list[:]
            minScore(my_list)
        elif option==11:
            prev_list=my_list[:]
            multiples(my_list)
        elif option==12:
            prev_list=my_list[:]
            deleteValue(my_list)
        elif option==13:
            prev_list=my_list[:]
            deleteLower(my_list)
        elif option==14:
            my_list=prev_list[:]
            print("The new list is: ",my_list)
        else:   print("Invalid option \n")
        
        
        
startProgram()
    