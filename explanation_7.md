Problem #7: HTTPRouter using a Trie
Design
I have implemented 3 classes: a router trie node, a router trie and a router. They have coresponding methods like:
Router trie node: initizalise and insert
router trie: initialize, insert and find
router: add_handler, lookup and split path

Big O Space Complexity
Splitting a string to store individual parts of the path is dependent on the length of the string and the depth or level of the path. This is large for a site with multiple web pages. Hence, using a dictionary the complexity should be O(n) where n is the count of components in the path.

Big O Time Complexity
we have to traverse the children to find the path and for any handler we have O(n) worst case.