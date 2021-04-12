def memo_fibo(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    FibArray = [0, 1]  
      
    while len(FibArray) <= n :  
        FibArray.append(0)             	#Append 0 to initialize it
    if n <= 1:                         	#Exit condition: 
        return n  				#We know that F(0) = 0, F(1) = 1
    else:  
        if FibArray[n - 1] == 0:        #F(n-1) done ?
            FibArray[n - 1] = memo_fibo(n - 1)  #No. Do it and save result
  
        if FibArray[n - 2] == 0:                #F(n-2) done ?
            FibArray[n - 2] = memo_fibo(n - 2)  #No. Do it and save result
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]
#Driver code  
print(memo_fibo(5))
