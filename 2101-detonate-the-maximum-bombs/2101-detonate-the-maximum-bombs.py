from collections import deque
class Solution:
    
    def maximumDetonation(self,bombs: int) -> int:
        
        hashmap_bombs = {}
        n = len(bombs)
        max_bombs = 1
        
        for i in range(n):
            x,y,r = bombs[i]
            for j in range(n):
                x2,y2,_ = bombs[j]
                if i == j:
                    continue

                d = math.sqrt((x-x2)**2 + (y-y2)**2)
                if d <= r:
                    if i in hashmap_bombs:
                        hashmap_bombs[i].append(j)
                    else:
                        hashmap_bombs[i] = [j]

        for node in hashmap_bombs:
            
            bombs = deque([node])
            total = 0
            visited_bombs = set()

            while bombs:
                
                exploted_bomb = bombs.popleft()
                if exploted_bomb in visited_bombs:
                    continue

                total += 1  
                
                visited_bombs.add(exploted_bomb)
                reach_bombs = hashmap_bombs.get(exploted_bomb,[])

                for bomb in reach_bombs:
                    if bomb not in visited_bombs:
                        bombs.append(bomb)

                
            max_bombs = max(total, max_bombs)


        return max_bombs 

        # bombs empty? 1 <= 100
        # x 1 <= 100,000
        # y 1 <= 100,000
        # r 1 <= 100,000
        # same coords
