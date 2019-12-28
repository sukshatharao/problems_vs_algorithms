Problem #1: Finding the Square Root of an Integer
Design
I have followed the Babylonian method as described in the Wikipedia to find the square root. 
epsilon = 0.00001  -> is the error in our estimate


Big O Time Complexity
It should perform O(log n) where n is the input number to the function.
More explanation:
Error E at any step k, Ek = ek * n ; n is the number
Therefore the algorithm will terminate once number - square of estimate < epsilon
which means accuracy is less than estimate error of epsilon
it will converge at , ek < 2 power(-f(k))
by logarithmic summation O(log(log(n)) approx


Big O Space Complexity
There is one float and three integer variables, although one is a counter to keep track of the number of iterations for my reference. This can be eliminated. Space complexity should be O(n) where n is the number of variables in the function which is five inclusive of the "number" passed into the function.