class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        # misunderstood the problem
        # def connected_servers(row: int, col: int) -> int:
        #     directions = [(1,0),(0,1),(-1,0),(0,-1)]
        #     queue = deque([(row,col)])
        #     total = 1
        #     grid[row][col] = 0

        #     while queue:
        #         row, col = queue.popleft()
                
        #         for dr, dc in directions:
        #             new_row = dr + row
        #             new_col = dc + col

        #             if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
        #                 queue.append((new_row,new_col))
        #                 total += 1
        #                 grid[new_row][new_col] = 0
            
        #     return total if total > 1 else 0

        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        total = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1

        for row in range(m):
            for col in range(n):

                if grid[row][col] == 1 and (rows[row] > 1 or cols[col] > 1):
                    total += 1

        return total