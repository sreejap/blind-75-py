#https://leetcode.com/problems/longest-palindromic-substring/editorial/
class Solution:
    # “A palindrome is defined by its center. 
    # Since I don’t know the center in advance, I try every index as a center for odd-length palindromes and every adjacent pair as a center for even-length palindromes, and expand outward.”
    # Pick a center, Expand outward, Track the longest
    def longestPalindrome(self, s: str) -> str:
        def expand (i,j):
            while i >=0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1

        ans = (0,0)
        for i in range (len(s)):
            odd_substr = expand (i,i)

            even_substr = expand (i,i+1)

            if odd_substr[1] - odd_substr[0] > ans[1] - ans[0]:
                ans = odd_substr
            
            if even_substr[1] - even_substr[0] > ans[1] - ans[0]:
                ans = even_substr

        return s [ans[0]:ans[1]+1]
