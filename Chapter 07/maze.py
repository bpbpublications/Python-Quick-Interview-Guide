from typing import List
class Solution:
    def solveMaze(self, maze:List[List[int]] )->List[int]: #Main function
#####################Define other nested functions        
        # A utility function to check if x, y is valid 
        def isSafe( maze, x, y ): 
            if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
                return True
            return False        
        #### A recursive utility function to solve Maze problem 
        def solveMazeUtil(maze, x, y, path): 
            # if (x, y) is goal, return True 
            if x == N - 1 and y == N - 1 and maze[x][y]== 1: 
                path[x][y] = 1  #Mark x,y as part of path
                return True
            # Check if maze[x][y] is valid 
            if isSafe(maze, x, y):
                path[x][y] = 1 #Temporarily add x,y to path
                # Try right and down neighbours
                if solveMazeUtil(maze, x + 1, y, path):return True
                if solveMazeUtil(maze, x, y + 1, path):return True
                # If none of the above movements work then  
                # BACKTRACK: unmark x, y as part of solution path 
                path[x][y] = 0
                return False    
 ####################Restart main       
        N = len(maze)  
        # Creating a N * N matrix for solution path 
        path = [ [ 0 for j in range(N) ] for i in range(N) ] 
        if solveMazeUtil(maze, 0, 0, path) :return path
        return None
# Driver code
maze = [ [1, 1, 1, 1], 
         [1, 1, 0, 1], 
         [0, 1, 1, 0], 
         [1, 1, 1, 1] ] 
sol=Solution()
Path = sol.solveMaze(maze)
for row in Path:print(row)