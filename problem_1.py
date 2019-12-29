#!/usr/bin/env python
# coding: utf-8

# In[10]:


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
    
    low = 0
    high = number
    # For computing integral part 
    # of square root of number 
    while (low <= high) : 
        mid = int((low + high) / 2) 
          
        if (mid * mid == number) : 
            ans = mid 
            break
          
        # incrementing start if integral 
        # part lies on right side of the mid 
        if (mid * mid < number) : 
            low = mid + 1
            ans = mid 
          
        # decrementing end if integral part 
        # lies on the left side of the mid 
        else : 
            high = mid - 1
    return ans

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




