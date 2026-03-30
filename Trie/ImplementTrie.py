class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.is_end = False

    def put (self, ch, node):
        # add node
        self.links [ord(ch) - ord ('a')] = node
    
    def get (self, ch):
        return self.links [ord(ch) - ord('a')]
    
    def contains_key (self,ch):
        return self.links [ord(ch) - ord('a')] is not None

class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.contains_key(c):
                node.put(c,TrieNode())
            node = node.get(c)
        node.is_end = True

    def search_prefix (self, word:str):
        node = self.root
        for c in word:
            if not node.contains_key(c):
                return None
                # add the empty trie node so that we could add chars
            node = node.get(c)
        return node
        
    def search(self, word: str) -> bool:
        node = self.search_prefix (word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
