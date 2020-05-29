class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.t
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['is_word'] = True
    
    def _search(self, word, is_prefix = False):
        t = self.t
        for char in word:
            if char not in t:
                return False
            t = t[char]
        
        if is_prefix:
            return True
        else:
            return 'is_word' in t
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(word, is_prefix=False)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search(prefix, is_prefix=True)