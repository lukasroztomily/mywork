#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:13:46 2021

@author: erik
"""




def sudd (n):
  st = n
  su = 0
  i = 1  
  while(i <= st):
        su = su +1
        if (su%2) ==0: 
            i = i + 1
            print(su)
        
    
# sudd(10)


def powers(base, n):
  st = n
  su = 0
  i = 1  
  while(i <= st):
        su = su +1
        print(base**su)
        i = i + 1

# 1 2 4 8 16 32 64 128 256 512
#powers(2, 10)



def divisors(n):
  st = n
  su = 0
  i = 1  
  for a in range(1, st+1):
        su = su +1  
        if (st%su) == 0: 
            print(su)

# 1 2 7 14
#divisors(100)

d = 10

def spr (n):
    for t in range(1, 1 + n):
        pass
        #if t>0:
         #print(t)

for a in range(1, 1+d):
    b = a - 6
    if b>0:
        #print(b)
        spr(b) 

n = 10
m = list()
n = n - 6
for t in range(n+1):
    if t >0:
        for a in range(t):
            if a > 0:
             m.append(a)
        m.append(t)
#print(m)


def c (v):
    o = list()
    for a in range(1, v+1):
        o.append(a)
        o.append(a*-1)
    return o
        
#print(c(5))

import mysql.connector
from mysql.connector import errorcode


config = {
  'user': 'Solo',
  'password': 'prase',
  'host': 'localhost',
  'database': 'webgarbage',
  'raise_on_warnings': True
}


p = str()
for e in range(1, 1+10):
    p += " "+str(e)
    
#print(p)    


a = 5
q = '  '
m = list()
for t in range(1, a+1):
    q += ' '+str(t)
    
    m.append(t)
q +='\n'
q +='   '        
q += '_ '*a
q +='\n'
for t in range(a):
   # print(m[t]) 
    v = m[t]
    o = t+1
    
    q += '\n'+str(o)+'|'
    for k in m:
        q += ' '+str(o*k)
print(q)
        


a = 5
q = '  '
m = list()
for t in range(1, a+1):
    q += ' '+str(t)
    
    m.append(t)
q +='\n'
q +='   '        
q += '_ '*a
q +='\n'
for t in range(a):
   # print(m[t]) 
    v = m[t]
    o = t+1
    
    q += '\n'+str(o)+'|'
    for k in m:
        q += ' '+str(o**k)
print(q)

a = 5
q = '  '
m = list()
for t in range(1, a+1):
    q += ' '+str(t)
    
    m.append(t)
q +='\n'
q +='   '        
q += '_ '*a
q +='\n'
for t in range(a):
   # print(m[t]) 
    v = m[t]
    o = t+1
    
    q += '\n'+str(o)+'|'
    for k in m:
        q += ' '+str(max(o, k))
print(q)
        

a = 5
q = '  '
m = list()
for t in range(1, a+1):
    q += ' '+str(t)
    
    m.append(t)
q +='\n'
q +='   '        
q += '_ '*a
q +='\n'
for t in range(a):
   # print(m[t]) 
    v = m[t]
    o = t+1
    
    q += '\n'+str(o)+'|'
    for k in m:
        q += ' '+str(o%k)
print(q)

# try:
#   cnx = mysql.connector.connect(**config)
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()

p = 5


z = str()
m = list()
for t in range(1, p+1):
    
    z+='\n'+str(t)+ ' #'
    z+='#'*(p-1)
print(z)

p = 7


z = str()
m = list()
for t in range(1, p+1):
    
    z+='\n'+ ' #'
    if t == 1:
      z+='#'*(p-2)+ '#'
    elif t == p:
        z+='#'*(p-2)+ '#'
    else:
        z+='.'*(p-2)+ '#'
        
    
print(z)
        


p = 5
tt = p//2
ttt = p//1.5
ttt = int(ttt)
print(ttt)
z = str()
m = list()
for t in range(1, p+1):
    

    if t == 1:
      z+=' '*(p)+'#'+' '*(p)+'\n'
    elif t == p:
        z+='# '*(p*2)
    elif t == tt:
        z+='   '*(tt//2)+'# '*(tt*2)+'  '*(tt//2)+'\n'
    elif t==ttt:
         z+='  '*(ttt//2)+'# '*(tt*2)+'  '*(ttt//2)+'\n'
        
    
print(z)



# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern triangle
def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("# ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 25
triangle(n)

# Python program to print nXn Assuming that n 
# is always even as a checkerboard was
  
import numpy as np
  
# function to print Checkerboard pattern
def printcheckboard(n):
      
    print("Checkerboard pattern:")
  
    # create a n * n matrix
    x = np.zeros((n, n), dtype = int)
  
    # fill with 1 the alternate rows and columns
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
      
    # print the pattern
    for i in range(n):
        for j in range(n):
            print(x[i][j], end =" ") 
        print()           
#    print(x)
  
# driver code
n = 9
printcheckboard(n)


n = 9
a = np.resize([2, 1], n)
x  = np.abs(a-np.array([a]).T)
for i in range(n):
   for j in range(n):
            print(x[i][j], end =" ") 
   print()
   
n= 9    
z = str()
nn = n//2
for t in range(1, n):
   if nn == t: 
     z +='\n##'+'#'*n
     
   else: 
     z +='\n#'+' '*n+'#'
    
    
print(z)    
n= 76    
for t in range(1, n+1):
    if (n%t) == 0:
        print(t)

n= 76    
for t in range(1, n+1):
    if (n%t) == 0:
        print(t)

      
def five():
    # vracime nejakou hodnotu
    return 50

def double(a):
    # vracime nejakou vypoctenou hodnotu
    b = a * 2
    return b        # mohlo by byt nahrazeno jen 'return a * 2'

def nothing():
    # tady je return pouzit jen k ukonceni provadeni funkce, ale nic se nevraci
    return

def without_return():
    # tady se muze dit neco zajimavenho, ale nic se nevraci
    pass

# vypisy vracenych hodnot
print(five())
print(double(21))
print(nothing())         # return bez hodnoty vrací speciální hodnotu None
print(without_return())  # stejne tak funkce bez return

# dalsi vyuziti vracenych hodnot
x = five()         # vracenou hodnotu si ulozime do promenne
y = double(x)
print(x, y)

print(double(five()))                            # pouziti primo v parametrech
print(range(five()))
print(double(double(double(double(five())))))    # ... opakovane


def my_max(number1, number2):
    if not isinstance(number1, int) or not isinstance(number2, int):
        print("jedno z cisel neni int")
        return
    if number1 == number2:
        print("jsou stejna")
        return number1
    if number1 > number2:
        print("prvni je vetsi")
        return number1
    # sem se vypocet dostane jen v pripade,
    # ze vsechny podminky v predhazejicich if neplati
    print("druhe je vetsi")
    return number2

print(my_max(2, "a"))
print("--------------")
print(my_max("a", 2))
print("--------------")
print(my_max(2, 2))
print("--------------")
print(my_max(2, 3))
print("--------------")
print(my_max(3, 2))


n= 10
v = 0    
for t in range(1, n+1):
    if (n%t) == 0:
        v = v + 1
        
print(v)



n= 127
v = list()    
for t in range(1, n+1):
    if (n%t) == 0:
        v.append(t)
        
print(v)


import math

print(math.e)
print(math.pi)
print(range(five()))


n =  3
qq = 1
for t in range(1, n+1):
    qq = qq * t
    
    
#print(qq)


p = 0
i = 0
st = 0
while i <= p:
    st += 1
    if (st%2)>0:
       # print(st)
        i += 1
        

p = 5
i = 0
kk = 0
while  i<p and kk < p:
    kk += 1
    if (kk%2)>0 :
        if kk < p :
            print(kk)
        i += 1  
                