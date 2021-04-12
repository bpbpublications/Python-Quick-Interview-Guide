import timeit
from matplotlib import pyplot as plt

def fibo(n):
    if n <= 1:
       return n
    else:
       return(fibo(n-1) + fibo(n-2))

su='''
from __main__ import fibo,i;
'''  
x=[]
y=[]   
for i in range(1,15):
    t=timeit.timeit('fibo(i)',setup=su,number=100)
    x.append(i)
    y.append(t)
plt.plot(y)
plt.xlabel("N->")
plt.ylabel("time")
plt.title("Time complexity of Fibonacci function")
    
 