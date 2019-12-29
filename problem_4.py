#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    Reference:
    #https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    """

def sort_012(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1
    # for a different type of list
    # middle value could be passed in for comparision
    mid_value = 1
    while mid <= high:
        if input_list[mid] < mid_value:
            # swap input_list[low] & input_list[mid]
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] > mid_value:
            # swap input_list[mid] & input_list[high]
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
        else:
            mid += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print("sorted array is ",sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0, 1, 2])


# In[ ]:




