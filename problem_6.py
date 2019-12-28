#!/usr/bin/env python
# coding: utf-8

# In[5]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) ==0:
        return False, False
    
    min = max = ints[0]
    for element in ints:
        if element <= min:
            min = element
        elif element >= max:
            max = element
    return min,max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((False, False) == get_min_max([])) else "Fail")
print("Pass" if ((99, 99) == get_min_max([99])) else "Fail")
print("Pass" if ((-2, 2) == get_min_max([0,0,-1,-1,0,-2,1,0,2,1])) else "Fail")
print("Pass" if ((99, 99) == get_min_max([99,99])) else "Fail")


# In[ ]:




