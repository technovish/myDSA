#Trie is tree based data structure that organizes information in heirarchy
#can have any number of child 
#Used to store and search strings in time and space effiecient way, any node can store non repetive multiple characters, every node links to next character of string,
#keeps track of end of strings, Used in spell check and auto completion
#Operations: Creation, Insertion, Deletion and Search for string in trie

class Node:
    def __init__(self):
        self.children = {}
        self.eos = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.eos = True


trie = Trie()
trie.insert("apple")

    



