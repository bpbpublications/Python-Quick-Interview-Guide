def memo2_fibo(n): 
    fn_2 = 0
    fn_1 = 1
    if n<2:
        return n
    else: 
        for i in range(2,n+1): 
            ans = fn_1 + fn_2 
            fn_2 = fn_1
            fn_1 = ans 
        return ans  
#Driver code  
print(memo2_fibo(9))
