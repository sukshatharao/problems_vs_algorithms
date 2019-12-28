#!/usr/bin/env python
# coding: utf-8

# In[44]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) ==0:
        return False
    if sum(input_list)== 0:
        return input_list
    mid = len(input_list)//2
   # list1 = merge_sort(input_list[:mid])
   # list2 = merge_sort(input_list[mid:])
   # result = [int("".join([str(item) for item in list1]))]
   # result.append(int("".join([str(item) for item in list2])))
    result = merge_sort(input_list)
    final = [int("".join([str(result[i]) for i in range(0, len(result),2)]))]
    final.append(int("".join([str(result[i]) for i in range(1, len(result), 2)])))
    return final

def merge_sort(input_list):
    mid = len(input_list)//2
    if len(input_list) <=1:
        return input_list
    list1 = merge_sort(input_list[:mid])
    list2 = merge_sort(input_list[mid:])
    return merge(list1,list2)

def merge(list1,list2):
    left_index = 0
    right_index = 0
    result = []
    list1_length = len(list1)
    list2_length = len(list2)
    while left_index < list1_length and right_index < list2_length:
        if list1[left_index] > list2[right_index]:
            result.append(list1[left_index])
            left_index += 1
        else:
            result.append(list2[right_index])
            right_index += 1
    
    while left_index < len(list1):
        result.append(list1[left_index])
        left_index += 1
    
    while right_index < len(list2):
        result.append(list2[right_index])
        right_index += 1
    
    return result
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    #print(output)
    solution = test_case[1]
    if not output:
        print("oops ! empty input?")
    
    elif sum(output) == sum(solution):
        print("Pass")
     
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [42, 531]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[],[]])
print(rearrange_digits([1, 2, 3, 4, 5]))
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
print(rearrange_digits([0, 2, 4, 6, 8]))
print(rearrange_digits([11, 9, 3, 9]))
test_function([[1, 1, 1, 3, 5, 6], [631, 511]])
test_function([[], [-1, -1]])
test_function([[0], [0]])
test_function([[0, 0], [0, 0]])


# In[ ]:




