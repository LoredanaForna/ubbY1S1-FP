'''
Created on 7 Nov 2017

@author: Lore
'''
import numpy as np

def addScalarNumpy(list,scalar):
    #the function adds a scalar to all the elements of a vector
    #I:the list with the value
    #O:the modified list
    list=np.array(list)
    if scalar==0:
        return list
    else:
        list+=scalar
        return list    
def sumvect(v1,v2):
    s=[]
    for i in range(len(v1)):
        s.append(v1[i]+v2[i])
    return s
def add(list,l1):
    '''
    D:function which adds 2 vectors
    I:the list of vectors and the new list for adition
    O:the list of new vectors
    '''
    new_list=[]
    for i in range(len(l1)):
        new_list.append(sumvect(l1[i],list[i]))
    return new_list
def addNumpy(list,l1):
    '''
    D:function which adds 2 vectors
    I:the list of vectors and the new list for adition
    O:the list of new vectors
    '''
    list=np.array(list)
    list=list+l1
    return list
def subvect(v1,v2):
    s=[]
    for i in range(len(v1)):
        s.append(v1[i]-v2[i])
    return s
def subb(list,l1):
    '''
    D:function which substracts 2 vectors
    I:the list of vectors and the new list for subctraction
    O:the list of new vectors
    '''
    new_list=[]
    for i in range(len(l1)):
        new_list.append(subvect(list[i],l1[i]))
    return new_list
def subbNumpy(list,l1):
    '''
    D:function which substracts 2 vectors
    I:the list of vectors and the new list for subctraction
    O:the list of new vectors
    '''
    list=np.array(list)
    list=list-l1
    return list
def multiplication(list,l1):
    '''
    D:function which multiplies 2 vectors
    I:the list of vectors and the new list for multiplication
    O:the list of new vectors
    '''
    lst=[]
    for i in list:
        sumv=[0]*len(l1[0])
        indice1=0
        for k in l1:
            indice2=0
            for p in k:
                no=i[indice1]*p
                sumv[indice2]+=no
                indice2+=1
            indice1+=1
        lst.append(sumv)
    return lst
 
def mulNumpy(list,l1):
    '''
    D:function which multiplies 2 vectors
    I:the list of vectors and the new list for multiplication
    O:the list of new vectors
    '''
    list=np.array(list)
    lst=[]
    lst=np.dot(list,l1)
    list=list.tolist()
    return lst        
def sum(list):
    '''
    D:function which adds the values of all vectors
    I:the list of vectors 
    O:the sum of values
    '''
    s=0
    for i in range(len(list)):
        for j in range (len(list[i])):
            s=s+list[i][j]
    return s
def sumNumpy(list):
    '''
    D:function which adds the values of all vectors
    I:the list of vectors 
    O:the sum of values
    '''
    s=[]
    list=np.array(list)
    s1=np.sum(list)
    list.tolist()
    return s1
def product(list):
    '''
    D:function which multiplies the values of all vectors
    I:the list of vectors 
    O:the product of values
    '''
    p=1
    for i in range(len(list)):
        for j in range (len(list[i])):
            p=p*list[i][j]
    return p
def productNumpy(list):
    '''
    D:function which multiplies the values of all vectors
    I:the list of vectors 
    O:the product of values
    '''
    list=np.array(list)
    s=[]
    for i in range(len(list)):
        x=np.prod(list[i])
        s.append(x)
    s1=np.prod(s)
    list.tolist()
    return s1
def average(list):
    '''
    D:function which computes the average of all vectors
    I:the list of vectors 
    O:the average of values
    '''
    nr=0
    sum=0
    for i in range(len(list)):
        for j in range (len(list[i])):
            sum=sum+list[i][j]
            nr=nr+1
    return sum/nr
def averageNumpy(list):
    '''
    D:function which computes the average of all vectors
    I:the list of vectors 
    O:the average of values
    '''
    list=np.array(list)
    s=np.average(list)
    return s
def minimum(list):
    '''
    D:function which finds the minimum from all vectors
    I:the list of vectors 
    O:the minimum
    '''
    mini=3000000
    for i in range(len(list)):
        for j in range (len(list[i])):
            if mini>list[i][j]:
                mini=list[i][j]
    return mini
def minNumpy(list):
    '''
    D:function which finds the minimum from all vectors
    I:the list of vectors 
    O:the minimum
    '''
    list=np.array(list)
    aux=list.min()
    list=list.tolist()
    return aux
def maximum(list):
    '''
    D:function which finds the maximum from all vectors
    I:the list of vectors 
    O:the maximum
    '''
    maxi=-300000
    for i in range(len(list)):
        for j in range (len(list[i])):
            if maxi<list[i][j]:
                maxi=list[i][j]
    return maxi
def maxNumpy(list):
    '''
    D:function which finds the maximum from all vectors
    I:the list of vectors 
    O:the maximum
    '''
    list=np.array(list)
    aux=list.max()
    list=list.tolist()
    return aux
def sumScalar(list,scalar):
    '''
    D:function which adds a scalar with a vector
    I:the list of vectors and a number
    O:the modified list
    '''
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j]=list[i][j]+scalar
    return list

