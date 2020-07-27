'''
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isword = False
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self
        for char in word:
            if char in current.children:
                pass
            else:
                node = Trie()
                current.children[char] = node
            current = current.children[char]
        current.isword = True
                
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self
        if not word:
            return False
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True if current.isword else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self
        if not prefix:
            return False
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True