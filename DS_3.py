# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:04:51 2021

@author: ISHA
"""

#list,tuple,dictionary,frozenset,enumerate,string,zip

#heterogeneous and homogeneous

#array =[1,2,3]

#array = [1,1.3,'hi',[True]

#mutable or changeable

#ordered or unordered 

#indexed


#list -- unordered data types
''' iterative element with more than 1 element'''
L1 =[2,1,3,4]
print (L1)
type(L2)
#list is kind of unordered data

L2 =['Isha',True,1,5.6]
L2
print (L2)
type(L2)
#heterogeneous

L2[0]
L2[1]
L2[2]
L2[3]
#indexed
L2[4] #index error :list out of range

#iterative
for i in L2:
    print (i)
#space -- indentation

len(L2)

r1 = range(50,10,-5)
type(r1)
r1


lr1 = list(r1)
lr1
len(lr1)
#lenght of list

r1 = range(20,50)
type(r1)
r1


lr1 = list(r1)
len(lr1)
lr1


r2 = range(10,20,5)
r2
type(r2)

lr2 = list(r2)
lr2


#specific element in list
lr1[1:4]
lr1[2:6]
lr1[3:]

lr1
lr1[::2]

lr1[::-1]
lr1[-3:-1]

lr1 = [18,15,20,25,10,15,1,45]
lr1
lr1.count(15)

#mutable list --- any element can be changed in list

lr[1]= 55
lr1

'''
    do not return anything
    a = lr1.append(40)       
    a
    
'''
    
    
#add an element at last
lr1.append(90)
lr1

#remove one element
lr1.remove(10)
lr1


#del specific element
del lr1[0]
lr1

del lr1
lr1

#returns some value that is popped out

a = lr1.pop()
lr1
a

b = lr1.pop(3)
b


lr2 = [10,15,20,25,10,15,10,45]
lr2


lr1.clear()
lr1

lr2 = list(range(10,50))
lr2
 
#empty list
lr1=[]

for i in lr2:
    lr1.append(i)
    print(lr1)

lr3 = lr1
lr3
lr1


#reverse of list
lr1.reverse()
lr1
lr1[::-1]


#similar elements grouped together
lr1.sort()
lr1


hi = ['a','e','o','u']
hi
hi.insert(2, 'i')
hi



#set

#not allow to duplicate the element

s1 = {1,2,3,5}
s1

#heterogeneous

s2 = {'hi',True,3}
s2

#not indexed
#ordered list of elements

s1 = {2,4,1,0,3}
s1

s1[0]  #type index error --> set object is subscriptable

for i in s1 :
    print(i)

#mutable
s1.add(4)
s1

s1.add(5)
s1


#add more than one element
s1.update([10,20])
s1

s1.discard(20)
s1

s1.pop()
s1

s1.pop(1)  #TypeError: pop() takes no arguments (1 given)
s1               

s1.clear()
s1

del s1


teamA = {'India','australia','pakistan','England'}
teamB = {'New Zealand','India','Bangladesh','West indies'}


teamA.union(teamB)

teamA.intersection(teamB)


#in teamA not in teamB
teamA.difference(teamB)



























