class Solution:  
    def generate(self, num_rows):  
        answer = []  # Collection of rows  
  
        for n in range(num_rows):  
            #Create initial version of nth row  
            # The first and last row elements are always 1.  
            # Let middle elements be 0  
            row = [0 for dummy in range(n+1)]  
            row[0], row[-1] = 1, 1  
            #Now fill middle elements  
            # Each  element of nth row is equal to the sum of the elements  
            # above-and-to-the-left and above-and-to-the-right.  
            #Let j span the nth row  
            for j in range(1, len(row)-1):  
                row[j] = answer[n-1][j-1] + answer[n-1][j]  
            #nth row is ready. append it to answer  
            answer.append(row)  
  
        return answer  
sol = Solution()  
print(sol.generate(6))  

