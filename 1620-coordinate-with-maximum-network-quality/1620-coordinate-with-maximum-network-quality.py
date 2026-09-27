import math
class Solution:
    def bestCoordinate(self, towers: list[list[int]], radius: int) -> list[int]:
        # radius ? lenght? 
        # lenght of towers 
        
        x_min, x_max = 50,0
        y_min, y_max = 50,0

        for x,y,_ in towers:
            x_min = min(x, x_min)
            x_max = max(x, x_max)
            y_min = min(y, y_min)
            y_max = max(y, y_max)

        q_max = 0
        coords_max = [0,0]

        for x in range(x_max, x_min-1, -1):
            for y in range(y_max, y_min-1, -1):
                total = 0

                for x_tower,y_tower,q_tower in towers:
                    d = math.sqrt((x_tower - x)**2 + (y_tower - y)**2)
                    
                    if d <= radius:
                        total += math.floor(q_tower / (1 + d))
                # print(f"coords: ({x},{y}), total: {total}")
                if total > q_max:
                    coords_max = [x,y]
                    q_max = total
                elif total == q_max:
                    if x < coords_max[0] or (x == coords_max[0] and y < coords_max[1]):
                        coords_max = [x,y]
        
        return coords_max