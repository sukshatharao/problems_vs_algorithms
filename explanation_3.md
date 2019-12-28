Problem #3: Rearrange Array Elements
Design
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. Rearranging array elements will always yield the sum of the digits regardless of order. As such it is possible to arrange the digits in multiple ways and always get the sum of the digits.

Divides the list in half and uses a recursive merge sort to create list of digits.

Big O Space Complexity
Merge sort creates a copy of the entire list, so space complexity is O(n)

Big O Time Complexity
In worst case time complexity O(n log(n)).