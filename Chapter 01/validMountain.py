from typing import List  #Not needed when submitting to Leet code
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False # A must have at leat 3 elements
        ascending = True#Set ascending state
        for i in range(len(A)-1):
            if A[i] == A[i+1]: return False #Two consecutive el must not be equal
            if ascending: 
                if A[i] > A[i+1]: ascending = False # Descending state set
            else:
                if A[i] <= A[i+1]: return False #Check descending condition
        #Ensure that ascending and descending sequences exist
        if A[-2] > A[-1] and A[0] < A[1]:#Ensure that ascending and desc
            return True
        else: return False
nums = [0,1,2,3,4,5,6,7,8,9]
sol = Solution()
print(nums)
print(sol.validMountainArray(nums))



