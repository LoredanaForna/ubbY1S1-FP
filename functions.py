'''
Created on 7 Nov 2017

@author: Lore
'''
import numpy as np
from app.ImpF import *


def test_addScalarNumpy():
    #this function will do the asserts for the function addScalar
    b=addScalarNumpy([[0]],2)
    c=[[2]]
    assert np.all(b==c)==True
    b=addScalarNumpy([[1,2],[1,1]],2)
    c=[[3,4],[3,3]]
    assert np.all(b==c)==True
    b=addScalarNumpy([[1,2,1,1,1,1,1]],10)
    c=[[11,12,11,11,11,11,11]]
    assert np.all(b==c)==True
    b=addScalarNumpy([[1],[1]],2)
    c=[[3],[3]]
    assert np.all(b==c)==True
    b=addScalarNumpy([5],2)
    c=[8]
    assert np.all(b==c)==False
def test_maxNumpy():  
    #this function will do the asserts for the function maxNumpy
    b=maxNumpy([[0]])
    c=0
    assert np.all(b==c)==True
    b=maxNumpy([[1,2],[1,1]])
    c=2
    assert np.all(b==c)==True
    b=maxNumpy([[1,2,1,1,1,1,1]])
    c=2
    assert np.all(b==c)==True
    b=maxNumpy([[1],[1]])
    c=1
    assert np.all(b==c)==True
    b=maxNumpy([5,10])
    c=11
    assert np.all(b==c)==False

def test_minNumpy():  
    #this function will do the asserts for the function minNumpy
    b=minNumpy([[0]])
    c=0
    assert np.all(b==c)==True
    b=minNumpy([[1,2],[1,1]])
    c=1
    assert np.all(b==c)==True
    b=minNumpy([[1,2,1,-1,1,1,1]])
    c=-1
    assert np.all(b==c)==True
    b=minNumpy([[1],[1]])
    c=1
    assert np.all(b==c)==True
    b=minNumpy([5,10])
    c=2
    assert np.all(b==c)==False
def test_averageNumpy():
    #this function will do the asserts for the function averageNumpy
    b=averageNumpy([[0]])
    c=0
    assert np.all(b==c)==True
    b=averageNumpy([[1,2],[1,1]])
    c=7
    assert np.all(b==c)==False
    b=averageNumpy([[1,1]])
    c=1
    assert np.all(b==c)==True
    b=averageNumpy([[3],[1]])
    c=2
    assert np.all(b==c)==True
    b=averageNumpy([5,10])
    c=2
    assert np.all(b==c)==False 

def test_sumNumpy():
    #this function will do the asserts for the function sumNumpy
    b=sumNumpy([[0]])
    c=0
    assert np.all(b==c)==True
    b=sumNumpy([[1,2],[1,1]])
    c=7
    assert np.all(b==c)==False
    b=sumNumpy([[1,1]])
    c=2
    assert np.all(b==c)==True
    b=sumNumpy([[3],[1]])
    c=4
    assert np.all(b==c)==True
    b=sumNumpy([5,10])
    c=17
    assert np.all(b==c)==False
def test_mulNumpy():
    #this function will do the asserts for the function mulNumpy
    b=mulNumpy([[0]],[[1]])
    c=[[0]]
    assert np.all(b==c)==True
    b=mulNumpy([[1,2,3],[10,12,23]],[[4,2],[1,2],[1,2]])
    c=[[9,12],[75,90]]
    assert np.all(b==c)==True
    b=mulNumpy([[3]],[[1]])
    c=[[3]]
    assert np.all(b==c)==True
    b=mulNumpy([5,10],[1,1])
    c=[[2],[3]]
    assert np.all(b==c)==False


def test_sumScalar():
    #this function will do the assertions for the function sumScalar
    assert sumScalar([[1,2,3],[0,0,0]],2)==[[3,4,5],[2,2,2]]
    assert sumScalar([[0,0,0],[0,0,0]],2)==[[2,2,2],[2,2,2]]
    assert sumScalar([[1,2,3],[1,2,3]],2)==[[3,4,5],[3,4,5]]
    assert sumScalar([[0,1,5],[10,15,20]],2)==[[2,3,7],[12,17,22]]
    assert sumScalar([[1,2,3],[0,0,0]],2)==[[3,4,5],[2,2,2]]
    assert sumScalar([[1,0,0],[0,0,0]],2)==[[3,2,2],[2,2,2]]
    
def test_productNumpy():
    #this function will do the asserts for the function productScalar
    b=productNumpy([[0]])
    c=0
    assert np.all(b==c)==True
    b=productNumpy([[1,2],[1,1]])
    c=2
    assert np.all(b==c)==True
    b=productNumpy([[1,2,1,1,11,1,1]])
    c=22
    assert np.all(b==c)==True
    b=productNumpy([[100],[1]])
    c=100
    assert np.all(b==c)==True
    b=productNumpy([5])
    c=8
    assert np.all(b==c)==False

def test_maximum():
        #this function will do the assertions for the function maximum
    assert maximum([[1,2,3],[0,0,0]])==3
    assert maximum([[0,0,0],[0,0,0]])==0
    assert maximum([[1,2,3],[1,2,3]])==3
    assert maximum([[0,1,5],[10,15,20]])==20
    assert maximum([[1,2,3],[0,0,0]])==3
    assert maximum([[0,0,0],[0,0,0]])==0 
def test_minimum():
        #this function will do the assertions for the function minimum
    assert minimum([[1,2,3],[0,0,0]])==0
    assert minimum([[0,0,0],[0,0,0]])==0
    assert minimum([[1,2,3],[1,2,3]])==1
    assert minimum([[0,1,5],[10,15,20]])==0
    assert minimum([[1,2,3],[0,0,0]])==0
    assert minimum([[0,0,0],[0,0,0]])==0
def test_average():
        #this function will do the assertions for the function average
    assert average([[1,2,3],[0,0,0]])==1
    assert average([[0,0,0],[0,0,0]])==0
    assert average([[1,2,3],[1,2,3]])==2
    assert average([[0,1,5],[10,15,20]])==8.5
    assert average([[1,2,3],[0,0,0]])==1
    assert average([[0,0,0],[0,0,0]])==0
def test_product():
        #this function will do the assertions for the function product
    assert product([[1,2,3],[0,0,0]])==0
    assert product([[0,0,0],[0,0,0]])==0
    assert product([[1,2,3],[1,2,3]])==36
    assert product([[0,1,5],[10,15,20]])==0
    assert product([[1,2,3],[0,0,0]])==0
    assert product([[0,0,0],[0,0,0]])==0
def test_sum():
        #this function will do the assertions for the function sum
    assert sum([[1,2,3],[0,0,0]])==6
    assert sum([[0,0,0],[0,0,0]])==0
    assert sum([[1,2,3],[1,2,3]])==12
    assert sum([[0,1,5],[10,15,20]])==51
    assert sum([[1,2,3],[0,0,0]])==6
    assert sum([[0,0,0],[0,0,0]])==0
def test_multiplication():
        #this function will do the assertions for the function multiplication
    assert multiplication([[1,2,3],[0,0,0]],[[0,0],[0,0],[0,0]])==[[0,0],[0,0]]
    assert multiplication([[0,0,0],[0,0,0]],[[0,0],[0,0],[0,0]])==[[0,0],[0,0]]
    assert multiplication([],[])==[]
    assert multiplication([[1,2,3],[10,12,23]],[[4,2],[1,2],[1,2]])==[[9,12],[75,90]]
    assert multiplication([[1,2,3],[1,1,1]],[[1,1],[0,0],[0,0]])==[[1,1],[1,1]]
    assert multiplication([[0,0,0],[0,0,0]],[[0],[0],[0]])==[[0],[0]]  
def test_subb():
     #this function will do the assertions for the function subb
    assert subb([[1,2,3],[0,0,0]],[[1,2,3],[0,0,0]])==[[0,0,0],[0,0,0]]
    assert subb([[0,0,0],[0,0,0]],[[2,2,2],[2,2,2]])==[[-2,-2,-2],[-2,-2,-2]]
    assert subb([[1,2,3],[1,2,3]],[[2,2,2],[2,2,2]])==[[-1,0,1],[-1,0,1]]
    assert subb([[0,1,5],[10,15,20]],[[2,2,2],[2,2,2]])==[[-2,-1,3],[8,13,18]]
    assert subb([[1,2,3],[0,0,0]],[[2,2,2],[2,2,2]])==[[-1,0,1],[-2,-2,-2]]
    assert subb([[0,0,0],[0,0,0]],[[2,2,2],[2,2,2]])==[[-2,-2,-2],[-2,-2,-2]]
def test_add():
    #this function will do the assertions for the function add
    assert add([[0,0,0],[0,0,0]],[[2,2,2],[2,2,2]])==[[2,2,2],[2,2,2]]
    assert add([[1,2,3],[1,2,3]],[[2,2,2],[2,2,2]])==[[3,4,5],[3,4,5]]
    assert add([[0,1,5],[10,15,20]],[[2,2,2],[2,2,2]])==[[2,3,7],[12,17,22]]
    assert add([[1,2,3],[0,0,0]],[[2,2,2],[2,2,2]])==[[3,4,5],[2,2,2]]
    assert add([[0,0,0],[0,0,0]],[[2,2,2],[2,2,2]])==[[2,2,2],[2,2,2]]

