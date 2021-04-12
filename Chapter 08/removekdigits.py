class Solution:
    def removeKdigits(self, num: str, k: int) -> str: #greedy??"
        num = [int(x) for x in list(num)]
        idx = 0
        #Do till the delete target k is reached
        while k > 0:
            #If only one number is left, return "0"
            if len(num) == 1:
                num[0] = 0
                break
            #if first number is bigger, 
            #delete it, decrement k and make idx=0
            if num[idx] > num[idx+1]:
                del num[idx]
                idx = 0
                k -= 1
            #Ifthe first number is less than or equal to second
            else:
                if idx == len(num)-2: #Consider corner
                    del num[idx+1]
                    idx = 0
                    k -= 1
                else:       #Don't delete yet, increment idx
                    idx += 1
        return str(int("".join(str(x) for x in num)))
#Driver code
sol=Solution()
num = "1432219"; k = 3
#num = "10200"; k = 1
#num = "123"; k = 1
print(sol.removeKdigits(num,k))