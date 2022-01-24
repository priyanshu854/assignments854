#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 1

# Q = Write a Python program to find those numbers which are divisible by 7
#      and multiple of 5, between 1500 and 2700 both included

# In[1]:


list=[]
a= range(1505,2702,7)

for i in a:
    if i%5==0:
        list.append(i)
print(len(list))        
        
    


# Q = Python program to add two numbers

# In[2]:


x = lambda a,b: a+b
print(x(2,5))


# In[3]:


def func_sum(a,b):
    c=a+b
    print(c)


# In[4]:


func_sum(2,5)


# Maximum of two numbers in Python

# In[5]:


c=4
d=8
x= max(c,d)

print(x)


# Python Program for factorial of a number

# In[6]:


a=int(input())
fact=1
m= range(1,a+1)
for i in m:
    fact=fact*i

print(fact)


# Python Program for simple interest

# In[ ]:


si = lambda p,q,r: p*q*r
print(si(1000,0.1,2))


# Python Program for compound interest

# In[ ]:


ci=lambda p,q,r:p*(1+r)**q - p
print(ci(1000,2,0.1))


# Python Program to check Armstrong Number

# In[ ]:


sum=0
list1=[]
number = str(input())
m= range(0,len(number))
for i in m:
         list1.append(int((number)[i])**len(number))
for i in m:
    sum=sum+list1[i]
    
if int(number)==print(sum):
        print('number is armstrong')
else:
        print('number is not armstrong')    
    


# In[ ]:


r=int(input())
area=3.14*r**2

print(area,end='unit^2')


# Python program to check whether a number is Prime or not

# In[ ]:


num=int(input())
if num> 1:
    for i in range(2,num):

        if (num%i)==0:
           print(num,"is not prime ")
           break
    else:
        print(num,'is  prime')
else:
    print('num is less than 1')
            


# In[ ]:




