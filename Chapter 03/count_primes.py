'''
class Solution:
    def countPrimes(self, n: int) -> int:		
        if n<2:                         #Base cases
            return 0
        count = 0
        for i in range(2,n):
            if self.isPrime(i): 
                count += 1
        return count
    def isPrime(self,n:int)-> bool:
        for i in range(2,n):
            if n%i == 0: return False
        else: return True
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0	  #Base cases  
        prime = [True for i in range(n)] #Create an array of n True elements 
        prime[0]=prime[1]=False          # We know 0 and 1 are not primes
        p = 2
        while (p * p < n):    #Same as p < sqrt(n)
        # Check if p is prime so far
            if (prime[p] == True): 
            # Mark all multiples of p as non prime
                for i in range(p * p, n, p): 
                    prime[i] = False
            p += 1
        return sum(prime)
sol = Solution()
print(sol.countPrimes(12))