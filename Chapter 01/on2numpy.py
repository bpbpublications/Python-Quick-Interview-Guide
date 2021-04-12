import numpy as np
x = np.array([[9,7,3],
              [4 ,1,6],
              [7 ,8,9]])
y = np.array([[5,8,1],
             [6,1,3],
             [4,5,9]])
result = np.matmul(x , y)
print(result)
