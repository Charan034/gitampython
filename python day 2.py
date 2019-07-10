#!/usr/bin/env python
# coding: utf-8

# In[4]:


# find the large number from 3 numbers
a1=int(input("enter the number 1 "))
a2=int(input("enter the number 2 "))
a3=int(input("enter the number 3 "))
if a1>a2 and a1>a3:
    print(a1,"is the large number")
elif a2>a1 and a2>a3:
    print(a2,"is the large number")
else :
    print(a3,"is the large number")


# In[9]:


# check if a year is leap year or not
year=int(input("enter the year"))
if year%400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("it is a leap year")
else :
    print("it is not a leap year")


# In[10]:


#need print "Gitam" for 5 times
x=0
while x<5 :
    print("Gitam")
    x=x+1


# In[2]:


# print n Natural numbers using while loop
n= int(input("enter the number "))
x=1
while x<=n :
    print(x ,end = " ")
    x=x+1


# In[1]:


n=int(input("enter the number "))
s=0
i=1
while i<=n:
    if i%2==0:
        s=s+i
    i=i+1
print(s)


# In[1]:


#number is number
#print the digits of given number : 3 2 1
n=int(input("enter the number"))
while n!= 0:
    r=n%10
    print(r,end = " ")
    n= n // 10


# In[13]:


#  read a number --1234 
#output -- 6(2+4)
def addEvenDigits(n):
    sum=0
    while n!=0:
        r=n%10
        if r%2 == 0:
            sum= sum + r
        n=n//10 
    return sum
addEvenDigits(1234)


# In[14]:


def printLarge(n):
    large=0
    while n!=0:
        r=n%10
        if large < r:
            large = r
        n=n//10 
    return large
printLarge(19528)


# In[16]:


#read the number as inputs
#output reverse of the given number
def reverseNumber(n):
    rev=0
    while  n!=0:

        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
reverseNumber(123)
    


# In[19]:


def  pallindrome(n):
    rev=0
    buffer=n
    while  n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if buffer ==rev:  
        return "yes"
    else :
        return "no"
print(pallindrome(123))   
print(pallindrome(121))


# In[21]:


#function to print n natural number using for loop
def printNnaturalnumbers(n):
    for x in range(1,n+1):
       print(x,end=" ")
    return 
printNnaturalnumbers(10)


# In[23]:


#function print the numbers between two limits
def printseries(lb,ub):
    for x in range(lb,ub+1):
        print(x,end=" ")
    return
printseries(11,25)


# In[25]:


def alternateNumbers(lb,ub):
    for x in range(lb,ub+1,4):
        print(x,end=" ")
    return
alternateNumbers(100,150)


# In[28]:


def reverseRange(start,end):
    for x in range(end,start-1,-1):
        print(x,end=" ")
    return
reverseRange(1,10)


# In[ ]:




