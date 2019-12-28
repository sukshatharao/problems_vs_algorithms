#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[37]:


from collections import defaultdict
class TrieNode:
    def __init__(self, word = None):
        ## Initialize this node in the Trie
        self.children = defaultdict(TrieNode) #dict()
        self.is_word = False

    def insert(self, word):
        ## Add a child node in this Trie
        for char in word:
            self = self.children[char]
        self.is_word = True

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        result = []
        node = self
        for s in suffix:
            if s in node.children:
                node = node.children[s]
            else:
                return result
        self.find_letters(node, suffix, result)
        return result

    def find_letters(self, node, letters, result):
       
       # create a list to store words for every TrieNode in children (letter => node)
       # if node is a leaf, append letter to list of words
       # if node isnt a word : list of words += recursive call to collect letters
        for key, next_node in node.children.items():
            if next_node.is_word:
                result.append(letters+key)
            self.find_letters(next_node, letters+key, result)

    def find_word(self, word):
        ## Find the Trie node that represents this prefix
        if self is None:
            return None
        node = self
        for char in word:
            if char not in node.children:
                return (False, False)
            node = node.children[char]
        return node.is_word


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[38]:


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if self.root is None:
            return None
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def find_word(self, prefix):
        ## Find the Trie node that represents this prefix
        if self.root is None:
            return None
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return (node.is_word, node.word)

    def find_words(self, suffix):
        if self.root is None:
            return None
        if suffix == '':
            return None
        node = self.root
        return node.suffixes(suffix)
        


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[39]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[40]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find_words(prefix)
        if prefixNode:
            print('\n'.join(prefixNode))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:





# In[ ]:




