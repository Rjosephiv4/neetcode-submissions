class TreeNode:
    def __init__(self):
        self.isWord = False
        self.children = {}




class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if not (letter in curr.children):
                curr.children[letter] = TreeNode()
            
            curr = curr.children[letter]
        
        curr.isWord = True


        

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if not (letter in curr.children):
                return False
            curr = curr.children[letter]

        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if not (letter in curr.children):
                return False
            curr = curr.children[letter]

        return True

        
        