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
        n = len(grid)
        m = len(grid[0])
        queue = []
        total_time = -1
        fresh_orange = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        
        if fresh_orange == 0:
            return 0
        

        while queue:
            current_size_stack = len(queue)
            total_time += 1

            for _ in range(current_size_stack):
                x,y = queue.pop(0)
                
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for row,column in directions:
                    new_row = x + row
                    new_column = y + column

                    if 0 <= new_row < n and 0 <= new_column < m:
                        
                        if grid[new_row][new_column] == 1:
                            queue.append((new_row, new_column))
                            grid[new_row][new_column] = 2
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
