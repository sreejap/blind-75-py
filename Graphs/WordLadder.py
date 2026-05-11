# https://leetcode.com/problems/word-ladder/
from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        # “If I access a key that doesn’t exist yet, create it with an empty list.”
        all_combo_dict = defaultdict(list) 

        for word in wordList:
            for i in range (L):
                all_combo_dict [word[:i] + "*" + word[i+1:]].append(word)  #note: get this pattern correct
        
        #bfs queue
        begin_queue = deque ([beginWord])
        end_queue = deque ([endWord])

        #visited with distance
        begin_visited = {beginWord:1}
        end_visited = {endWord:1}

        # add the helper method here
        def visit (queue, visited, other_visited):
            for _ in range (len(queue)):
                word = queue.popleft()
                for i in range (L):
                    pattern = word[:i] + "*" + word [i+1:]
                    for nei in all_combo_dict [pattern]:
                        if nei in other_visited:
                            return visited[word] + other_visited[nei]
                        if nei not in visited:
                            visited[nei] = visited[word] + 1
                            queue.append (nei)
            return None
        while begin_queue and end_queue:
            if len(begin_queue) <= len (end_queue):
                ans = visit (begin_queue, begin_visited, end_visited)
            else:
                ans = visit (end_queue, end_visited, begin_visited)
            
            if ans:
                return ans
        
        return 0
