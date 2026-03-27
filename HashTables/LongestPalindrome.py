class Solution:
    def longestPalindrome(self, s: str) -> int:
       # t(c)- o(N) 
       # s(c) - o(1) because 52 chars
        char_set = set() # abccccdd
        res = 0
        for c in s:
            if c in char_set:
                res += 2
                char_set.remove(c)
            else:
                char_set.add(c) # adding to set

        if len(char_set)!=0:
            res += 1        
        return res
