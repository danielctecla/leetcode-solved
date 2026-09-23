from collections import deque
class Solution:
    # def orangesRotting(self, grid: list[list[int]]) -> int:
        
# grid n x m
# 0 x 0? no
# no rotten orange, and not fresh orange?

# n x m
# grid = [[2,1,1],[1,1,0],[0,1,1]]
# I travel the matrix looking for the rotten orange
# [[0][0]] save the rotten orange in a stack
# START LOOP
#   check the 4-adjacent orange of rotten oranges.
#   convert to rotten orange and add to the stack
#   BFS - Stack
#   for each iteration in the entire loop +1 the counter time
# finally I return the time of the rotten orange.
    
    def orangesRotting(self, grid: list[list[int]]) -> int:
        r, c = len(grid), len(grid[0])
        root_oranges = deque()
        total_time = -1
        fresh_orange = 0

        for row in range(r):
            for col in range(c):
                if grid[row][col] == 2:
                    root_oranges.append((row,col))
                elif grid[row][col] == 1:
                    fresh_orange += 1
        
        if fresh_orange == 0:
            return 0
        

        while root_oranges:
            total_time += 1

            for _ in range(len(root_oranges)):
                row,col = root_oranges.popleft()
                
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if 0 <= nr < r and 0 <= nc < c:
                        
                        if grid[nr][nc] == 1:
                            root_oranges.append((nr, nc))
                            grid[nr][nc] = 2
                            fresh_orange -= 1

        return total_time if fresh_orange == 0 else -1


            
# grid = [
#[2,2,1],
#[2,1,0],
#[0,1,1]]

# total_time = 2
# stack = []

# first loop - double for  O(nxm)

#stack = [(0,1),(1,0)]
