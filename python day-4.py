#!/usr/bin/env python
# coding: utf-8

# In[6]:


lst=[1,8,18,9,27]
print(lst)
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])
print(lst[1:])
print(lst[1:4])
print(lst[-3:])


# In[7]:


li=["Gitam","Python",1989,2002]
print(li)
li[2]=2019
print(li)


# In[8]:


#delete the specific item in the list
print(li)
del li[2]
print(li)


# In[9]:


#basic list operations
lst1=[1,9,6,18,2]
print(len(lst1))#length of the list
print(lst1 *2) #repeatation
print(len(lst1))
print(9 in lst1)#list item is present or not
print(15 in lst1)#access the list iteam by iteration
for x in range(len(lst1)):
    print(lst1[x],end=" ")


# In[10]:


#function of the list
lst1
print(min(lst1)) #min item/element of the list
print(max(lst1))#Max item of the list
print(sum(lst1))#sum of all elements of the list
print(sum(lst1)//len(lst1))#average of the list elements
print(sum(lst1[1::2])/len(lst1[1::2])) #average of the elements


# In[15]:


lst1=[1,2,4,18,12]
lst1.append(24) #adding a new element at the end of the list
lst1
lst1.insert(2,56) #adding an element at particular index
lst1
lst1.count(4) #return the value how many times the object repeated
lst1.index(56)
lst1.sort() #it's sort the list in ascending order
lst1
lst1.pop() #remove the last element from the list
lst1
lst1.pop(1) #remove an element from a particular index
lst2=[123,23,45]
lst1.extend(lst2) # merge the list2 into the list1
lst1.reverse()
lst1.remove(123)
lst1

 


# In[23]:


# functions to find the second large item from the list
def secondlarge(li):
    li.sort()
    return li[-2]
def genericLarge(li,n):
    li.sort()
    return li[-n]
li=[1,19,6,2,8,18,3]
genericLarge(li,4)


# In[24]:


#function to find the least item of the list
def secondlist(li):
    li.sort()
    return li[1]
def genericLarge(li,n):
    li.sort()
    return li[n-1]
li=[1,19,6,2,8,18,3]
genericLarge(li,2)


# In[30]:


##linear search
#function to search the data in the list
def linearsearch1(li,tarItem):
        for x in range(len(li)):
            if li[x] ==tarItem:
                return x
        return -1
li=[1,19,6,2,8,18,3]
linearsearch1(li,6)
                


# In[29]:


#function
#input :[1,5,9,6,5,15,1,2,5 ]key=5 #duplicate
#output : 1,4,8
def linearsearch2(li,tarItem):
    for x in range (len(li)):
        if li[x] == tarItem:
            print(x,end =" ")
    return
li=[1,5,9,6,5,15,1,2,5]
linearsearch2(li,5)


# In[36]:


#function 
#input :List
# output :seq of the characters
#test case
#[1,5,9,6,5,15,1,2,5 ],tar=5 -- !! !!!!! !!!!!!!!!
def linearsearch3(li,tarItem):
    for x in range (len(li)):
        if li[x] == tarItem:
            j=0
            while j!=x+1:
                print("!",end ="")
                j=j+1
            print(end =" ")
    return
li=[1,5,9,6,5,15,1,2,5]
linearsearch3(li,5)


# In[37]:


#function
#input :list
#output : formatted
#test case:
# [12,2,45,9,8,15,36]--60
#a list is perfectely multiple of 3 and 5
def linearsearch4(li):
    sum=0
    for x in range(len(li)):
        if li[x] %3==0 and li[x] %5==0:
            sum += li[x]
    return sum
li=[12,2,45,9,8,15,36]
linearsearch4(li) #60


# In[38]:


#function
#input : list
#output :formatted  output
#test case
#[1,2,3,4,5] --[1,3,8,15,5]
#[6,5,2,8,2] --[6,12,40,4,2]
def linearsearch5(li):
    for x in range(len(li)):
        if x==0 or x==len(li)-1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li=[1,2,3,4,5]
linearsearch5(li)
       


# In[43]:


#function
#input : list
#output :formatted  output
#test case
#[1,6,9,4,16,19,22] --1 9 19 22
def linearsearch6(li):
    for x in range(len(li)):
        if x==0 or x==len(li)-1:
            print(li[x],end=" ")
        elif li[x-1]%2 ==0 and li[x+1]%2 ==0:
            print(li[x],end=" ")
    return
li=[1,6,9,4,16,19,22]  
linearsearch6(li)


# #numbers to list
# Input as number
# Expected output as list
# 

# In[45]:


def numberlistconversation(n):
  li=[]
  while n!=0:
      r=n%10
      li.append(r)
      n=n//10
  li.reverse()
  return li
numberlistconversation(14569)
  


# In[48]:


#function to count the occurance of a character in a string
def countcharoccurance(s,c):
    cnt=0
    for ch in s:
        if ch ==c:
            cnt +=1
    return cnt
countcharoccurance("python programming","m")


# ### string to list converation
# #input will be string
# #expected output will be list

# In[53]:


#function to convert string to list
#test case 
def stringtolistconversation(s):
   li=s.split()
   numberslist=[]
   for i in li:
       numberslist.append(int(i))
   return numberslist
s="1 2 3 4 5 6"
stringtolistconversation(s)
                      


# 
# 

# ## sorting algorithms
# - Bubble sort
# - Selection sort
# - Insertion sort

# In[54]:


#function to represent the bubble sort
def bubblesort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li
li=[19,1,25,6,18,3]
bubblesort(li)
     


# In[ ]:




