# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:35:45 2021 ....17jan

@author: ISHA
"""
#static input
a = 10
b =1.5
c = True
country = 'India'
'''
no need to specify type of variable
like in other programming languages

'''

country1 = input()                      
print("is",country1)

country2 = input("live--> " )
print("--> ",country2)

print("i live in {0} and want to go {1}".format(country1,country2))
print("i live in {0} and want to go {1}".format(country,country1))
print("i live in {1} and want to go {0}".format(country1,country2))
'''
{0} - .format(xyz)
in same line {0}.... {1}  .format(0,1)
'''
#type casting or type conversion
a= 10
b = 12.5
c= '10'

af = float(a)
af
type(af)
print(af)

bi = int(b)
bi
type(bi)
print(bi)

bst = str(bi)
bst
type(bst)



#ascii
asc = chr(97)
asc

asc = chr(49)
asc


ascr = ord("A")
ascr

#assignment operations
x = 1
print(x+1)

x = 2
x = x+1
print(x)

a=1
a +=1
print(a)

a=9
print( a, a+1, a*2)


#power
x=3
print(x ** 2)

#root
x=64
print(x ** 1/3)


#and or not

t = True
f = False

print (t and f)
print (f and t)
print(f and f)
print (t and t)


d = 0
g = 1
print(d or g)
print(d or d)
print(g or g)

i = True
j = False
print(not i)


#adding two 
Fname = 'isha'
Lname = 'goel'
name = Fname + ' ' + Lname
name

print(len(name))

name.capitalize()
name

name.upper()
name

''' shift or centralize the string '''

name = "isha"
name = name.rjust(10)

name = 'isha'
name = name.ljust(10)

name ='love'
name = name.center(10)

print(name)

'''.replace('', '')  '''
s = 'hi i am isha'
s1 = s.replace('hi', 'hello')
s1

''' remove starting and last spacing '''

l = '         hii     '
k = l.strip()
k





