#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
A RouteTrieNode will be similar to our autocomplete TrieNode...
with one additional element, a handler.
"""
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = handler

    def insert(self, path, handler = None):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None, not_found = None):
        """
        Initialize the trie with a root node and a handler,
        this is the root path or home page node
        """
        self.root = RouteTrieNode()
        self.handler = handler
        self.not_found = not_found if not_found is not "" or not_found is not None else "HTTP 404 Page Not Found"

    def insert(self, path_list, handler):
        """
        Similar to our previous example you will want to recursively
        add nodes. Make sure you assign the handler to only the leaf
        (deepest) node of this path
        """
        node = self.root
        for path in path_list:
            if path not in node.children:
                node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self, path):
        """
        Starting at the root, navigate the Trie to find a match for
        this path. Return the handler for a match, or None for no match
        """
        if self.root is None:
            return self.not_found # None
        node = self.root
        for path_part in path:
            if path_part not in node.children:
                return self.not_found # None
            node = node.children[path_part]
        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler = None, not_found = None):
        """
        Create a new RouteTrie for holding our routes. You could also
        add a handler for 404 page not found responses as well!
        """
        self.root = RouteTrie(handler)
        self.handler = handler
        self.not_found = not_found if not_found is not "" or not_found is not None else "HTTP 404 Page Not Found"

    def add_handler(self, path, handler):
        """
        Add a handler for a path. You will need to split the path and
        pass the parts as a list to the RouteTrie
        """
        node = self.root
        path_list = self.split_path(path)
        node.insert(path_list, handler)

    def lookup(self, path):
        """
        Lookup path (by parts) and return the associated handler.
        You can return None if it's not found or return the "not found"
        handler if you added one.
        Bonus points if a path works with and without a trailing slash
        e.g. /about and /about/ both return the /about handler
        """
        if path == "/":
            return "This is root!"
        node = self.root.root
        path_list = self.split_path(path)
        for path_part in path_list:
            if path_part not in node.children:
                return "HTTP 404 Page Not Found"
            node = node.children[path_part]
        if not node.handler:
            return "HTTP 404 Page Not Found"
        return node.handler

    def split_path(self, path):
        """
        You need to split the path into parts for both the add_handler
        and lookup functions, so it should be placed in a function here
        """
        # if begins or ends with '/' they will be '' in the split list
        path_list = path.split('/')
        # discard the empty strings
        if path_list[0] == '':
            path_list = path_list[1:]
        if path_list[-1] == '':
            path_list = path_list[:-1]
        return path_list

# create the router and add a route
# remove the 'not found handler' if you did not implement this

router = Router("/", "root handler")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/menu", "menu")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# In[ ]:




