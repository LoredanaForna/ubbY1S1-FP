'''
Created on 30 Oct 2017

@author: Lore
'''
#prev_list=[]

import ImportantFunctions  
from ImportantFunctions import addNumber
from ImportantFunctions import insertNumber
from ImportantFunctions import remove1
from ImportantFunctions import sortedValues
from ImportantFunctions import mul


 #Feature 1 
  
def test_addNumber():
    
    #This program will do asserts in order to test the function addNumber
    assert addNumber([1,5,7,8,4],12)==[1,5,7,8,4,12]
    assert addNumber([2],123)==[2,123]
    assert addNumber([],18)==[18]
    assert addNumber([109],2)==[109,2]
    assert addNumber([-2,3],9)==[-2,3,9]

'''
addNumber(list,7) #7
addNumber(list,1) #7,1
addNumber(list,2) #7,1,2
addNumber(list,3) #7,1,2.3
addNumber(list,4) #7,1,2,3,4
addNumber(list,5) #7,1,2,3,4,5
addNumber(list,6) #7,1,2,3,4,5,6
addNumber(list,7) #7,1,2,3,4,5,6,7
addNumber(list,8) #7,1,2,3,4,5,6,7,8
addNumber(list,1) #7,1,2,3,4,5,6,7,8,1

'''     



def test_insertNumber():
    #the asserts which are necessary for testing our insertion function
    assert insertNumber([1,5,7,8,4],4,123)==[1,5,7,8,123]
    assert insertNumber([2],0,1)==[1,2]
    assert insertNumber([],0,1)==[1]
    assert insertNumber([11,11],1,11)==[11,11,11]
    assert insertNumber([1,3],2,3)==[1,3,3]
      
'''
my_list=[0,1,2,3,4,5,6,7,8,9,10]
insertNumber(list,1,5) #0,5,2,3,4,5,6,7,8,9,10
insertNumber(list,3,5) #0,5,2,5,4,5,6,7,8,9,10
insertNumber(list,12,4) #Error
insertNumber(list,7,1) #0,5,2,5,4,5,6,1,8,9,10
insertNumber(list,0,10) #10,5,2,5,4,5,6,1,8,9,10
insertNumber(list,2,5) #10,5,5,5,4,5,6,1,8,9,10
insertNumber(list,18,10) #Error
insertNumber(list,7,9) #10,5,5,5,4,5,6,9,8,9,10
insertNumber(list,2,1) #10,5,1,5,4,5,6,1,8,9,10
insertNumber(list,0,0) #0,5,1,5,4,5,6,1,8,9,10

'''

#Feature 2

def test_remove1():
    #this program will remove the element on index 1
    assert remove1([1,5,7,8,4])==[1,7,8,4]
    assert remove1([2])==[2]
    assert remove1([])==[]
    assert remove1([123])==[123]
    assert remove1([-2,3])==[-2]

'''
list=[1,2,3,4,5,6,0,7,8,9,10]

remove1(list,1) #1,3,4,5,6,0,7,8,9,10
remove1(list,1) #1,4,5,6,0,7,8,9,10
remove1(list,1) #1,5,6,0,7,8,9,10
remove1(list,1) #1,6,0,7,8,9,10
remove1(list,1) #1,0,7,8,9,10
remove1(list,1) #1,7,8,9,10
remove1(list,1) #1,8,9,10
remove1(list,1) #1,9,10
remove1(list,1) #1,10
remove1(list,1) #1
'''

def test_removeIndex():
    #this program will remove the element from index i to index j
    assert removeIndex([1,5,7,8,4],1,3)==[1,4]
    assert removeIndex([2],1,3)==[2]
    assert removeIndex([],1,3)==[]
    assert removeIndex([123,0,0,0,0,0,1],1,3)==[123,0,0,1]
    assert removeIndex([-2,3],1,3)==[-2]
    
def removeIndex(my_list):
    #the function will delete the value on index i to index j
    #I: the list
    #O:the list without the element on index i to index j
    i=int(input("Write the first index: "))
    j=int(input("Write the second index: "))
    while ((i>len(my_list)-1 or j>len(my_list)-1) or (i>len(my_list)-1 and j>len(my_list)-1)):  
        print("IndexError. Read another index")
        i=int(input("Write the first index:"))
        j=int(input("Write the second index:"))
    del(my_list[i:j+1])
    print(my_list)

'''
my_list=[123,0,0,0,1,2,3,10,4,5,6,7,8,11]
removeIndex(my_list)  #123,1,2,3,10,4,5,6,7,8,11
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)
removeIndex(my_list)

'''

def test_replaceValue():
    #the function will do the asserts for the function replaceValue
    assert replaceValue([1,3,4,7], 3, 45)==[1,3,4,45]
    assert replaceValue([],0,1)==[]
    assert replaceValue([1,2,3],0,2)==[2,2,3]
    assert replaceValue([10],4,9)==[10]
    assert replaceValue([19,100,12,8,46,7,21],6,100)==[19,100,12,8,46,7,100]
        
def replaceValue(my_list):
    #D:the function changes the value on index i with a specific value
    #I:the list,the index and the new value
    #O:the list which is modified
    i=int(input("Write an existent index: "))
    val=int(input("Write the value: "))
    if len(my_list)>=i:
       my_list[i]=val
    else:
        while i>len(my_list)-1:
            print("IndexError. Read another pair of indexes")
            i=int(input("Write an existent index"))
            val=int(input("Write the value: "))
        my_list[i]=val
    print(my_list)

'''
my_list=[0,1,2,3,4,5,6,7,8,9,10]
replaceValue(my_list,1,45) #0,45,2,3,4,5,6,7,8,9,10
replaceValue(my_list,9,18) #0,45,2,3,4,5,6,7,8,18,10
replaceValue(my_list,0,1) #1,45,2,3,4,5,6,7,8,18,10
replaceValue(my_list,5,9) #1,45,2,3,4,5,6,7,9,18,10
replaceValue(my_list,20,1) #1,45,2,3,4,5,6,7,9,18,10
replaceValue(my_list,4,10) #1,45,2,3,10,5,6,7,9,18,10
replaceValue([],9,18) #[]
replaceValue(my_list,1,11) #1,11,2,3,10,5,6,7,9,18,10
replaceValue([1,2,3],2,5) #[1,2,5]
replaceValue(my_list,7,999) #1,11,2,3,10,5,6,999,9,18,10
'''

#Feature 3

def test_printValue():
    #This function will test all the asserts for the function printScore
    assert printValue([90,71,0,8,40])==[2,3]
    assert printValue([40,89])==[0]
    assert printValue([1,2,3,55])==[0,1,2]
    assert printValue([])==[]
    assert printValue([19,8,11])==[1]

def printValue(my_list):
    #D:The function will print all the numbers in the list that are less than n
    #I:the list with the number that will be used in the condition for print
    #O:the numbers from the least that are less than the number n in a new list
    ok=0
    new_list=[]
    n=int(input("Write a number: "))
    for i in range(len(my_list)):
        if my_list[i]<n:
            ok=1
            new_list.append(i)
    if ok==1:
        print(new_list)
    else: print("There is not a number less than ",n)
    

'''
my_list=[91,71,0,101,8,40,400] #3,5
my_list=[40,89] #0
my_list=[1,2,3,55] #1,2,3
my_list=[] #0
my_list=[19,8,11] #1,2,3
my_list=[191,80,11,98]  #3
my_list=[400,7,40,1,40] #2,4
my_list=[21,41,50,78,90,111,22,4]    #1,7,8
my_list=[0,0,0]   #1,2,3
my_list=[90]   #0
'''

def test_sortedValues():
    #This function will test all the asserts for the function sortedPoints
    assert sortedValues([45,2,100,4,5,10])==[2,4,5,10,45,100]
    assert sortedValues([1,2,5,3])==[1,2,3,5]
    assert sortedValues([4,8,1,10,2])==[1,2,4,8,10]
    assert sortedValues([1,1,1])==[1,1,1]
    assert sortedValues([])==[]


'''               
sec_list=[45,2,100,4,5,10]
#sortedPoints(sec_list) #2,4,5,10,45,100
sec_list=[1,2,5,3]
#sortedPoints(sec_list) #1,2,3,5
sec_list=[4,8,1,10,2]
#sortedPoints(sec_list) #1,2,4,8,10
sec_list=[1,1,1]
#sortedPoints(sec_list) #1,1,1
sec_list=[]
#sortedPoints(sec_list) #[]
sec_list=[1,2,3,4,5]
#sortedPoints(sec_list) #1,2,3,4,5
sec_list=[5,4,3,2,1]
#sortedPoints(sec_list) #1,2,3,4,5
sec_list=[0]
#sortedPoints(sec_list) #[]
'''

def test_sortedAndGreater():
    #This function will test all the asserts for the function sortAndGreater
    assert sortedAndGreater([45,2,100,4,5,10])==[100]
    assert sortedAndGreater([45,2,10,4,5])==[]
    assert sortedAndGreater([])==[]
    assert sortedAndGreater([45,2,100,490,90,91])==[91,100,490]
    assert sortedAndGreater([90,90,90])==[]

def sortedAndGreater(my_list):
    #D:verifies if a number is greater than 90 & puts it in a new list and shows it at the end
    #I:the list
    #O:the new ordered list with the numbers >90 
    n=int(input("The number is: "))
    aux_list=[]
    for i in range(len(my_list)):
        if my_list[i]>n:
            aux_list.append(i)
    aux_list.sort()       
    print(aux_list)

'''
my_list=[45,2,100,490,90,91]
sortedAndGreater(my_list,90) #91,100,490
my_list=[90,71,0,8,40]
sortedAndGreater(my_list,90) #[]
my_list=[40,89]
sortedAndGreater(my_list,90) #[]
my_list=[1,2,3,55]
sortedAndGreater(my_list,90) #[]
my_list=[]
sortedAndGreater(my_list,90) #[]
my_list=[19,8,11]
sortedAndGreater(my_list,90) #[]
my_list=[191,80,11,98]
sortedAndGreater(my_list,90)  #98,191
my_list=[400,7,40,1,40]
sortedAndGreater(my_list,90) #400
my_list=[21,41,50,78,90,111,22,4]
sortedAndGreater(my_list,90)    #111
my_list=[0,0,0]
sortedAndGreater(my_list,90)    #[]
my_list=[91]
sortedAndGreater(my_list,90)    #91
'''

#Feature 4


def test_avgNumbers():
      #this function will run the asserts for the function avgNumbers
      assert avgNumbers([1,2,3,4,5],1,5)==[3]
      assert avgNumbers([],1,5)==[]
      assert avgNumbers([10,41,80,5,20,14,400,70],1,5)==[17.6]
      assert avgNumbers([10,40,10],1,5)==[20]
      assert avgNumbers([0,0,0],1,5)==[0]

'''
avgNumbers([1,2,3,4,5],1,5) #[3]
avgNumbers([],1,5)  #[]
avgNumbers([10,41,80,5,20,14,400,70],1,5)  #[17.6]
avgNumbers([10,40,10],1,5)  #[20]
avgNumbers([0,0,0],1,5)  #[0]
avgNumbers([10,20,50,0,90,6,5,30],1,5)   #[33.2]
avgNumbers([1,2,3,4,5,6,7],1,5)   #[4.0]
avgNumbers([0,0,0,0,0,1,1,1],1,5)  #[0.2]
avgNumbers([9,8,2,4,5,11,7],1,5)   #[6.0]
avgNumbers([1],1,5) #[1]
'''


def avgNumbers(my_list):
    #The function will print the average of the numbers between indexes i and j
    #I:the list
    #O:the average of the j-i+1 numbers from the list
    i=int(input("Write the first index: "))
    j=int(input("Write the second index: "))
    while ((i>len(my_list)-1 or j>len(my_list)-1) or (i>len(my_list)-1 and j>len(my_list)-1)):  
        print("IndexError. Read another pair of indexes")
        i=int(input("Write the first index:"))
        j=int(input("Write the second index:"))
    sum=0
    nr=0
    for k in range(i,j+1) :
        sum=sum+my_list[k]
        nr=nr+1
    avg=sum/nr
    if nr==0:
        print("The list is empty")
    else: 
        print("The average is: ", avg)
        
        
def test_minScore():
      #this function will run the asserts for the function minScore
      assert minScore([0,9,13,18],1,5)==[0]
      assert minScore([],1,5)==None
      assert minScore([10,41,80,5,20,14,400,70],1,5)==[5]
      assert minScore([0],1,5)==[0]
      assert minScore([11,11,11,11],1,5)==[11]
'''
minScore([0,9,13,18],1,5)  #[0]
minScore([],1,5)   #None
minScore([10,41,80,5,20,14,400,70],1,5)   #[5]
minScore([0],1,5)   #[0]
minScore([11,11,11,11],1,5)   #[11]
minScore([9,8,7,7,6,5,4],1,5)  #[4]
minScore([11,13,14,15,10,1817,12,13,13],1,5) #[10]
minScore([11,11,11,11,11],1,5)  #[11]
'''

def minScore(my_list):
    #The function will print the minimum from the list between index i and index j
    #I:the list
    #O:The minimum
    i=int(input("Write the first index: "))
    j=int(input("Write the second index: "))
    while ((i>len(my_list)-1 or j>len(my_list)-1) or (i>len(my_list)-1 and j>len(my_list)-1)):  
        print("IndexError. Read another pair of indexes")
        i=int(input("Write the first index:"))
        j=int(input("Write the second index:"))
    if len(my_list)==0:
        print(None)
    else:
        minimum=1000000
        for k in range(i,j+1):
            if minimum>my_list[k]:
                minimum=my_list[k] 
        print("The minimum is ",minimum)


 
def test_multiples():
    #this function will run the asserts for the function multiples
    assert multiples([10,41,80,5,20,14,400,70],10)==[80,20]
    assert multiples([0,9,1,2],10)==[]
    assert multiples([10,90,100,0,110,1,1,1,45],10)==[10,90,100,110]
    assert multiples([],10)==[]
    assert multiples([10,9,8,7,6,5,4,3,2,1],10)==[10]

'''
multiples([10,41,80,5,20,14,400,70],10) #[80,20]
multiples([0,9,1,2],10) #[]
multiples([10,90,100,0,110,1,1,1,45],10)  #[10,90,100,110]
multiples([],10)  #[]
multiples([10,9,8,7,6,5,4,3,2,1],10)  #[10]
multiples([1,10,100,10000],10)   #[10,100,10000]
multiples([1,2,3,4,5,6,7,8,9,0],10)  #[]
multipples([1],10)   #[]
'''

def multiples(my_list):
    #the function will print the numbers from the list that are multiples of 10
    #I:the list
    #O:a new list with all the numbers which are multiples of 10
    m=int(input("Write the number whose multiples will be printed:"))
    i=int(input("Write the first index: "))
    j=int(input("Write the second index: "))
    while ((i>len(my_list)-1 or j>len(my_list)-1) or (i>len(my_list)-1 and j>len(my_list)-1)):  
        print("IndexError. Read another pair of indexes")
        i=int(input("Write the first index:"))
        j=int(input("Write the second index:"))
    new_list=[]
    k=i
    while k<=j:
        if mul(my_list[k],m)==1:
            new_list.append(my_list[k])
        k=k+1
    print(new_list)
    

#Feature 5

def test_deleteValue():
    #the function will do the asserts for the function deleteValue
    assert deleteValue([1,2,3,45],5)==[1,2,3]
    assert deleteValue([12,189,122],5)==[12,189,122]
    assert deleteValue([10,20,30],10)==[]
    assert deleteValue([],9)==[]
    assert deleteValue([90,9,18,2,4,6],9)==[2,4,6]

def deleteValue(my_list):
    #D:the function modifies the list such that it will delete the numbers which aren't multiples of n
    #I:the list with the number which is used in the condition
    #I:the list modified
    i=0
    n=int(input("Write the number whose multiples won't be deleted: "))
    while i in range(len(my_list)):
        if mul(my_list[i], n)==0:
            del(my_list[i])
            i=i-1
        else:
            i=i+1
    print(my_list)
    
    
'''
my_list=[0,1,2,3,4,15,665,100,13,223,24,12,1,18]
deleteValue(my_list,5) #[0,1,2,3,4,13,223,24,12,1,18]
deleteValue(my_list,3) #[0,1,2,4,15,223,1]
deleteValue(my_list,2) #[0,1,15,223,1]
deleteValue([],9) #[]
deleteValue([2,4,6],2) #[]
deleteValue([1,2,3,4,5,6,7,8,9],2) #[1,3,5,7,9]
deleteValue([1,2,3,4,4,5,6,7,8,9],3) #[1,2,4,4,5,7,8]
deleteValue([10,12,14],10) #[12,14]
deleteValue([12,2,24,64],4) #[2]
deleteValue([0,5,10,18],5) #[0,18]


'''
    
def deleteLower(my_list):
    #D:the function will delete the numbers which are less or equal to n
    #I:the list and the number which will be in the condition
    #O:the list modified
    i=0
    n=int(input("The list's numbers will be deleted if are less or equal to: "))
    while i in range(0,len(my_list)):
        if my_list[i]<=n:
            del(my_list[i])
        else:
            i=i+1
    print(my_list)
    

def test_deleteLower(my_list,n):
    #the function will do the asserts for the function deleteLower
    assert deleteLower([10,345,2,89],12)==[345,89]
    assert deleteLower([100,1000,19,678,120],1000)==[]
    assert deleteLower([],19)==[]
    assert deleteLower([67,59,60,69,70,76,45],67)==[69,70,76]
    assert deleteLower([90,91,98],19)==[90,91,98]
        
'''
deleteLower([1,2,3],1) #[2,3]
deleteLower([99,90,92],91) #[99,92]
deleteLower([],10) #[]
deleteLower([1,2,3,4,5,6],0) #[1,2,3,4,5,6]
deleteLower([1,2,3],4) #[]
deleteLower([10,901,78,45],50) #[901,78]
deleteLower([0,0,0],19) #[]
deleteLower([90,89,45,67,12],11) #[90,89,45,67,12]
deleteLower([4,5,6,7,8],7)    #[8]
deleteLower([9,8,7,6,5,4,3,2,1,0],10) #[]
deleteLower([10],10) #[]
'''

 
#def undo(my_list):
     #print(prev_list)
      