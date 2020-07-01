class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
        node.isEnd = True
    
    def _special_search(self, word, node, err):
        if err > 1:
            return False
        if not word:
            return (node.isEnd) and (err == 1)
        c = word[0]
        for candidate in node.children:
            res = self._special_search(word[1:], node.children[candidate], err + int(c != candidate))
            if res:
                return True
        return False
        
            

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = Trie()
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.record.insert(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.record._special_search(word, self.record.root, 0)
        
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)