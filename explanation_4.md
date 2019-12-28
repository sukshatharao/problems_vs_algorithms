Problem #4: Dutch National Flag Problem
Design
It divides input list using a three-way partitioning of the array as per the wikipedia. The element in the input list is compared with the mid value. it swaps the elements moving the zeroes to the beginning of the array and the twos towards the end and ones in the middle by comparing it with the mid value=1.

Big O Space Complexity
variables low, mid and high and variable to store the middle value
a copy of the input list/array: O(n). 
I swapped elements without temp variable

Big O Time Complexity
O(n) where n is the number of elements in the list.
I have to go through the entire list inorder to complete the swaps