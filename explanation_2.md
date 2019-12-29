Problem #2: Search in a Rotated Sorted Array
Design
I call the locate pivot function to locate the pivot. If it exists in the pivot position itself, then I return the pivot index. If not it proceeds to partition the input list recursively to find pivot. Then binary search is called on the first half of the partition or second half of the partition based on the pivot index.

Big O Space Complexity
Variable like pivot, low , high, mid are required to store the positions of the indices to make the traversal through the array. It takes O(n) space to store the input list and the space to store the additional variables;  n is the input size of the array/list. 

Big O Time Complexity
Finding the pivot point is similar to a binary search. Both begin by halving the input list in each iteration and continuing dividing it in half until we find the pivot point or the target value. Hence time complexity is O(log n);  n is the input size of the array/list. 
Since this is a recursive binary search implementation, there is stack space that is occupied. hence its space complexity is (log n)
O(1) is the complexity to find target value in first, middle or last position.
the solution contains recursive binary search implementation, please also mention briefly about the call stack space occupied by the algorithm.