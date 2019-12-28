#!/usr/bin/env python
# coding: utf-8

# In[150]:


import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number ==1:
        return number
    if number < 0:
        return False
    
    epsilon = 0.00001  #error in our estimate
    iterations = 0
    estimate = 1.0
    
    #while guess**2 <= number:
    while abs(number - estimate*estimate) > epsilon:   #Babylonian method - https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
        estimate = (estimate+ number/estimate) / 2.0
        iterations +=1
    return math.floor(estimate)

print ("Pass sqrt(9)" if  (math.sqrt(9) == sqrt(9)) else "Fail")
print ("Pass sqrt(0)" if  (math.sqrt(0) == sqrt(0)) else "Fail")
print ("Pass sqrt(16)" if  (math.sqrt(16) == sqrt(16)) else "Fail")
print ("Pass sqrt(1)" if  (math.sqrt(1) == sqrt(1)) else "Fail")
print ("Pass sqrt(27)" if  (math.floor(math.sqrt(27)) == sqrt(27)) else "Fail")
if sqrt(-11) == False: print ("Pass sqrt(-11)") 
print("Disclaimer1 --- please wait for sometime for the next square root to appear!!!")
print ("Pass sqrt(6241)" if (math.sqrt(6241) == sqrt(6241))   else "Fail sqrt(6241)")
print("Disclaimer2 --- please wait for sometime for the next square root to appear!!!")
print ("Pass sqrt(1562500)"  if (math.sqrt(1562500) == sqrt(1562500)) else "Fail sqrt(1562500)")
print("Pass sqrt(2)" if  (math.floor(math.sqrt(2)) == sqrt(2)) else "Fail")


# In[ ]:




