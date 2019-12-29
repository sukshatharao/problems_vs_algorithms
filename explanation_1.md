Problem #1: Finding the Square Root of an Integer
Design
I have followed used binary search to find the square root. 
hence i check if the number from 1 to n (n is the input) and calculate the mid
if mid*mid equals to the n , then return the mid.
else check if the mid*mid value is less than n -  calculate mid - mid (mid+1 ,high)
else if the mid*mid value is greater than n -  calculate mid - mid (0 , mid-1)

Big O Time Complexity
It should perform O(log n) where n is the input number to the function.
The complexity is similar to the binary search since the logic used is like binary search
which goes on halving the array at every cycle


Big O Space Complexity
There is one float and three integer variables, although one is a counter to keep track of the number of iterations for my reference. This can be eliminated. 
The number of variables is independent of the input to the function, the space complexity is O(1) in the worst-case big-O notation 
