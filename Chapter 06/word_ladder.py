from typing import List
from collections import defaultdict,deque
class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        # Find the length of the words
        L = len(beginWord)

        # Build Wildcard dictionary of the form
        # {*at:hat,h*t:hat,ha*:hat}
        wildcard_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                wildcard_dict[word[:i] + "*" + word[i+1:]].append(word)
        # Initialize Queue for BFS with beginWord, level 1
        queue = deque([(beginWord, 1)])
        # Maintain a list of visited words, initially beginWord
        visited = {beginWord}
        while queue:
            #for i in range(len(queue)):print(queue[i])
            popped_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words *at,h*t,ha*
                intermediate_word = popped_word[:i] + "*" + popped_word[i+1:]
                #Search intermediate word in wildcard dictionary
                for word in wildcard_dict[intermediate_word]:
                    if word == endWord: #Found the word?
                        return level + 1#Yes, return level+1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                wildcard_dict[intermediate_word] = []
        return 0
#Driver code
sol=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord,endWord,wordList))