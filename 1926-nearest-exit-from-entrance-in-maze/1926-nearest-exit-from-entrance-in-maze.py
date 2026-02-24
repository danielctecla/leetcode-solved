class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        stack = deque()
        stack.append((entrance,0))
        maze[entrance[0]][entrance[1]] = '+'
        rows = len(maze)
        cols = len(maze[0])
        while(stack):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            pos, step = stack.popleft()

            if (pos[0] == 0 or pos[0] == rows - 1 or pos[1] == 0 or pos[1] == cols - 1) and step != 0:
                return step

            for dr, dc in directions:
                
                if 0 <= pos[0] + dr < rows and 0 <= pos[1] + dc < cols:    
                    nr = pos[0] + dr
                    nc = pos[1] + dc

                    if maze[nr][nc] == '.':
                        maze[nr][nc] = '+'   # marcar vecino
                        stack.append(((nr, nc), step + 1))                   
        
        return -1