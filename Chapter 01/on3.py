# Program to multiply two matrices using nested loops
# Create 3x3 matrix X
X = [[9,7,3],
    [4 ,1,6],
    [7 ,8,9]]
# Create 3x3 matrix Y
Y = [[5,8,1],
    [6,1,3],
    [4,5,9]]
# Create empty result matrix

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
print(result)
