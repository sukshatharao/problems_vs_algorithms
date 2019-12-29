Problem #5: Autocomplete With Tries
Design
Uses a default dictionary to store each letters. Lookups and insertions should be faster than a BST (learnt from the class at Udacity).

Big O Space Complexity
with dictionary the worst case is O(n); where n is the number of characters in a string.
we have consider the recursive call to find_letters from suffixes. This function find_letters:
-create a list to store words for every TrieNode in children (letter => node)
-if node is a leaf, append letter to list of words
-if node isnt a word : list of words += recursive call to collect letters

hence find_letters occupies the auxillary space and then returns the result(which has appended letters in the TrieNode)
This depends on the number of letters that are there in the TrieNode or in the word

Big O Time Complexity
insertion and finding a word takes O(n); where n is the length of the search string.