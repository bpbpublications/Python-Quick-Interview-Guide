#from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if(n<2):
            return s
        left = 0    #Start of longest substring
        right = 0

        palindrome = [[0]*n for _ in range(n)]

        for j in range(1,n):
            for i in range(0,j):
                innerIsPalindrome = palindrome[i+1][j-1] or j-i<=2
                si=s[i]
                sj=s[j]
                if(s[i] == s[j] and innerIsPalindrome):
                    
                    palindrome[i][j] = True
                    if(j-i>right-left):
                        left = i
                        right = j
        print(palindrome)
        return s[left:right+1] 
sol = Solution()
print (sol.longestPalindrome('babad')) 
       