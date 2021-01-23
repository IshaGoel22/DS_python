# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:04:51 2021

@author: ISHA
"""

#list,tuple,dictionary,frozenset,enumerate,string,zip

#heterogeneous and homogeneous

#array =[1,2,3]

#array = [1,1.3,..]

#






#list
''' iterative element with more than 1 element'''
L1 =[2,1,3,4]

type(L1)
print (L1)
#list is kind of unordered data

L2 =['Isha',True,1,5.6]
print (L2)
type(L2)
#heterogeneous

L2[0]
L2[1]
L2[2]
L2[3]
#indexed

#iterative
for i in L2:
    print (i)
#space -- indentation

r1 = range(5)
r1
type(r1)

lr1 = list(r1)
len(lr1)

r1 = range(10,50)
r1
type(r1)

lr1 = list(r1)
lr1
len(lr1)


#specific element in list
lr1[1:4]
lr1[2:6]
lr1[3:]

lr1
lr1[::2]




lr1 = [10,15,20,25,10,15,10,45]

lr1.cout(15)

#mutable list --- any element can be changed in list

lr[1]= 55
lr1

a= lr1.remove(10)
lr1
a

del lr1[0]
lr1

del lr1
lr1

lr1 = [10,15,20,25,10,15,10,45]

lr1.clear()
lr1

lr2 = list(range(10,50))

lr2
 
#empty list
lr1=[]

for i in lr2:
    lr1.append(i)
    print(lr1)

