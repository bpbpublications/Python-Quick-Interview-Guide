class Solution:
    def romanToInt(self, s: str) -> int:
      #Create dictionary to convert roman symbols to value
      #roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
      roman2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      ans = 0 #initialize answer to 0
      while i < len(s): #Scan the string with i
         if i<len(s)-1 and s[i:i+2] in roman2:#First try to match double letter symbols
            ans+=roman2[s[i:i+2]]            #Add value to answer
            i+=2
         else:                              #Now try single letter symbols
            ans+=roman[s[i]]                #Add value to answer
            i+=1
      return ans
sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("CDXLIII"))
