class Node:
    def __init__(self):
        self.links = [None] * 26
        self.ends_with = 0
        self.prefix_count = 0
    def containsKey(self,i):
        return True if self.links[i] else False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            i = ord(i) - ord('a')
            if node.containsKey(i):
                node = node.links[i]
                node.prefix_count+=1
            else:
                newLink = Node()
                node.links[i] = newLink
                node = newLink
                node.prefix_count+=1
        node.ends_with+=1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for i in word:
            i = ord(i) - ord('a')
            if node.containsKey(i):
                node = node.links[i]
            else:
                return 0
        return node.ends_with

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for i in prefix:
            i = ord(i) - ord('a')
            if node.containsKey(i):
                node = node.links[i]
            else:
                return 0
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        for i in word:
            i = ord(i) - ord('a')
            if node.containsKey(i):
                node = node.links[i]
                node.prefix_count-=1
            else:
                return
        node.ends_with-=1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
