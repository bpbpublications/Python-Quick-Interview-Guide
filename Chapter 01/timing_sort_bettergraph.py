import timeit
import random
from matplotlib import pyplot as plt
a=[]
def sorta():
    a.sort()

su='''
from __main__ import sorta;
'''  
x=[]
y=[]   
for i in range(1,50):
    for j in range(i):
        a.append(random.randint(1,100))
    t=timeit.timeit('sorta()',setup=su,number=100)
    x.append(i)
    y.append(t)
plt.plot(y)
plt.xlabel("N->")
plt.ylabel("time")
plt.title("Time complexity of sort function")
    
 