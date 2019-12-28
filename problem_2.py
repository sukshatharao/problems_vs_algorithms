#!/usr/bin/env python
# coding: utf-8

# In[74]:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # find pivot element where the array is divided into two sorted halves
    #pivot is an index at which - next element is less than the value[pivot]
    
    pivot = locate_pivot(input_list, 0, len(input_list)-1)
    if number == input_list[pivot]:
        return pivot
    
    #check if the element is less or equals to the element at "pivot-1" and is greater or equals to first element at 0
    # in other words check if the element is in first half 
    elif number <= input_list[pivot-1] and number >= input_list[0]:
        return binary_search(number, input_list, 0, pivot-1)
    
    #check if the element is greater or equals to the element at "pivot+1" and is less or equals to last element
    # in other words check if the element is in second half
    elif number >= input_list[pivot+1] and number <= input_list[len(input_list)-1]: 
        return  binary_search(number, input_list, pivot+1 ,len(input_list)-1)
    
    #search the entire array as there is no pivot
    else:
        return binary_search(number, input_list, 0, len(input_list)-1)

def locate_pivot(input_list, low, high):
    if low > high: #checked the entire array
        return -1
    
    mid = (high+low)//2
    if mid < high and input_list[mid] > input_list[mid+1]: #check if mid value is greater than mid+1 -> mid is pivot
        return mid
    elif mid > low and input_list[mid-1] > input_list[mid]: #check if mid-1 value is greater than mid -> mid-1 is pivot
        return mid-1
    elif input_list[low] > input_list[mid]:
        return locate_pivot(input_list, low, mid-1)
    return locate_pivot(input_list, mid+1, high)
    
def binary_search(target, arr, low , high):
    mid = (low+high)//2
    if low > high:
        return -1
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(target, arr, low, mid-1)
    else: return binary_search(target, arr, mid+1, high)
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[12, 13, 14, 15, 16, 17, 18, 10, 11], 10])
test_function([[12, 13, 14, 15, 16, 17, 18, 10, 11], 13])
test_function([[16, 11, 12, 13, 14, 15], 11])


# In[ ]:




