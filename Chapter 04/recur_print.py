def printFunc(n): 
    if (n < 1): 
        return
    else: 
        print( n, end = " ") # 1
        printFunc(n-1)        # 2 
        print( n, end = " ") # 3
        return

printFunc(5) 