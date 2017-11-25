'''
Created on 7 Nov 2017

@author: Lore
'''
from app.ImpF import add, averageNumpy
from app.ImpF import multiplication
from app.ImpF import subb
from app.ImpF import sumScalar
from app.ImpF import sum
from app.ImpF import product
from app.ImpF import average
from app.ImpF import minimum
from app.ImpF import maximum
from app.Debug import debug
from app.ImpF import addScalarNumpy
from app.ImpF import addNumpy
from app.ImpF import subbNumpy
from app.ImpF import sumNumpy
from app.ImpF import productNumpy
from app.ImpF import minNumpy
from app.ImpF import maxNumpy
from app.ImpF import averageNumpy
from app.ImpF import mulNumpy
def readVector(l1,n,m):
    #the function will create a list of lists
    #I:the empty list l1 and the lengths m &n
    #O:the new list
    l1=[]
    for i in range(n):
        lst1=[]
        print("Vector ",i,":")
        for j in range(m):
            ok=0
            while(ok==0):
                try:
                    x=int(input("Give the element:"))
                    ok=1
                except ValueError:
                    print("The value it has to be an integer")
                    ok=0
            lst1.append(x)
        l1.append(lst1)
    return l1
def printMenu():
    menuStr="\n Menu: \n"
    menuStr+="\t Press 1 - Add a scalar to a vector  \n"
    menuStr+="\t Press 11 - Add a scalar to a vector with numpy  \n"
    menuStr+="\t Press 2 - Add two vectors \n"
    menuStr+="\t Press 22 - Add two vectors with numpy  \n"
    menuStr+="\t Press 3 - Subtract two vectors \n"
    menuStr+="\t Press 33 - Subtract two vectors with numpy \n"
    menuStr+="\t Press 4 - Multiply two vectors \n"
    menuStr+="\t Press 5 - Sum of elements in a vector \n"
    menuStr+="\t Press 55 - Sum of elements in a vector with numpy \n"
    menuStr+="\t Press 6 - Product of elements in a vector \n"
    menuStr+="\t Press 66 - Product of elements in a vector with numpy \n"
    menuStr+="\t Press 7 - Average of elements in a vector \n"
    menuStr+="\t Press 77 - Average of elements in a vector with numpy \n"
    menuStr+="\t Press 8 - Minimum of a vector \n"
    menuStr+="\t Press 88 - Minimum of a vector with numpy \n"
    menuStr+="\t Press 9 - Maximum of a vector \n"
    menuStr+="\t Press 99 - Maximum of a vector with numpy \n"
    menuStr+="\t Press 10 - Debug \n"
    menuStr+="\t Press 0 - EXIT \n"
    print(menuStr)

def startProgram():
    #the user interface  
    ok=0
    aux=[]
    while(ok==0):
        try:
            n=int(input("Give the number of vectors: "))
            ok=1
            if n<0:
                ok=0
        except ValueError:
            print("The value it has to be a positive number")
            ok=0
    ok=0
    while(ok==0):
        try:
            m=int(input("Give the length:"))
            ok=1
            if m<0:
                ok=0
        except ValueError:
            print("The value it has to be a positive number")
            ok=0
    list=[]
    list=readVector(list, n, m)
    print(list)
    printMenu()
    while(True):
        l1=[]
        option=int(input("Enter an option: "))
        if option==0:
            break
        elif option==1:
            while(ok==0):
                try:
                    scalar=int(input("The scalar is: "))
                    ok=1
                    if scalar<0:
                        ok=0
                except ValueError:
                    print("The value it has to be an integer")
                    ok=0
            print("The sum of a vector with a scalar is: ")
            list=sumScalar(list, scalar)
            print(list)
        elif option==11:
            while(ok==0):
                try:
                    scalar=int(input("The scalar is: "))
                    ok=1
                    if scalar<0:
                        ok=0
                except ValueError:
                    print("The value it has to be an integer")
                    ok=0
            print("The sum of a vector with a scalar is: ")
            list=(addScalarNumpy(list,scalar).tolist())
            print(list)
        elif option==2:
            l1=readVector(l1,n,m)
            list=add(list,l1)
            print(list)
        elif option==22:
            l1=readVector(l1,n,m)
            list=(addNumpy(list,l1).tolist())
            print(list)
        elif option==3:
            l1=readVector(l1, n, m)
            list=subb(list,l1)
            print(list)
        elif option==33:
            l1=readVector(l1,n,m)
            list=(subbNumpy(list,l1).tolist())
            print(list)
        elif option==4:
            ok=0
            while(ok==0):
                try:
                    n=int(input("Give the number of vectors you want to multiply with: "))
                    ok=1
                    if n<0:
                        ok=0
                except ValueError:
                    print("The value it has to be a positive number")
                    ok=0
            ok=0
            while(ok==0):
                try:
                    m=int(input("Give the length of the vectors:"))
                    ok=1
                    if m<0:
                        ok=0
                except ValueError:
                    print("The value it has to be a positive number")
                    ok=0
            l1=readVector(l1, n, m)
            list=multiplication(list,l1)
            print(list)
        elif option==44:
            ok=0
            while(ok==0):
                try:
                    n=int(input("Give the number of vectors you want to multiply with: "))
                    ok=1
                    if n<0:
                        ok=0
                except ValueError:
                    print("The value it has to be a positive number")
                    ok=0
            ok=0
            while(ok==0):
                try:
                    m=int(input("Give the length of the vectors:"))
                    ok=1
                    if m<0:
                        ok=0
                except ValueError:
                    print("The value it has to be a positive number")
                    ok=0
            l1=readVector(l1, n, m)
            list=(mulNumpy(list,l1).tolist())
            print(list)
        elif option==5:
            print("The sum of elements in a vector is: ")
            print(sum(list))
        elif option==55: 
            print("The sum of elements in a vector is: ") 
            aux=(sumNumpy(list).tolist())
            print(aux)
        elif option==6:
            print("The product of elements in a vector is: ")
            print(product(list))
        elif option==66:
            print("The product of elements in a vector is: ")
            aux=(productNumpy(list).tolist())
            print(aux)
        elif option==7:
            print("The average of elements in a vector is: ")
            print(average(list))
        elif option==77:
            print("The average of elements in a vector is: ")
            print(averageNumpy(list))
        elif option==8:
            print("The minimum of a vector is: ")
            print(minimum(list))
        elif option==88:
            print("The minimum of a vector is: ")
            print(minNumpy(list))
        elif option==9:
            print("The maximum of a vector is: ")
            print(maximum(list))
        elif option==99:
            print("The maximum of a vector is: ")
            print(maxNumpy(list))
        elif option==10:
                debug()
        else:
            print("This option doesn't exist.")
startProgram()  