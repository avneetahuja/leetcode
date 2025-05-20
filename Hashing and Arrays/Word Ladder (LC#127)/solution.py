class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)      
                        q.append((new_word, dist+1))

        return 0
