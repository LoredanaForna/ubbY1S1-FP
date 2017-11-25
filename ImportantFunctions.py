'''
Created on 30 Oct 2017

@author: Lore
'''
#from Features import prev_list
def addNumber(my_list):
    
    #D:The function will add the element elem in the list
    #I:the list and the element
    #O:the new list
    elem=int(input("Enter a value: "))
    my_list.append(elem)
    print(my_list)

def insertNumber(my_list):
    #D:The function will insert a value on a specific index of the list
    #I:the list with the elem we want to add and the position
    #O:the list modified with the new element
    i=int(input("Write an existent index:"))
    while(i>len(my_list)-1):
        print("IndexError. Read another index")
        i=int(input("Write an existent index:"))
    val=int(input("Write a value:"))
    my_list.insert(i,val)
    print(my_list)
        
def remove1(my_list):
    #the function will delete the value on index i
    #I: the list
    #O:the list without the element on index i
    i=int(input("Write an existent index: "))
    while(i>len(my_list)-1):
        print("IndexError. Read another index")
        i=int(input("Write an existent index:"))
    del(my_list[i])
    print(my_list)


def sortedValues(my_list):
    #D:the function sorts the numbers
    #I:the list
    #O:the ordered list 
    my_list.sort()
    print(my_list)
    
def mul(n,m):
      #The function will return 0 if n isn't a multiple of 10 or 1 if it is 
    ok=0
    i=1
    while i*m<=n:
         if i*m==n:
             ok=1 
         i=i+1
    return ok
